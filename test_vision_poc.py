#!/usr/bin/env python3
"""
Proof-of-Concept: Test AI Vision Extraction on Piping Drawings

This script tests the vision prompts with Claude Sonnet 4.5.
Usage:
    python test_vision_poc.py <path_to_pdf_or_image>
"""

import os
import sys
import json
import base64
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Anthropic client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def encode_image(image_path: str) -> str:
    """Encode image to base64 for API"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def extract_pipe_specs(image_path: str) -> dict:
    """Extract pipe specifications from drawing image"""
    
    # Read and encode image
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Determine media type
    ext = Path(image_path).suffix.lower()
    media_type_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    media_type = media_type_map.get(ext, "image/jpeg")
    
    # Encode image
    image_data = encode_image(image_path)
    
    # Vision prompt (complete extraction)
    prompt = """You are analyzing an isometric piping drawing to extract specifications for cost estimation.

Extract ALL of the following:

1. **Drawing Info:**
   - Drawing number
   - Title
   - Scale
   - Revision

2. **Pipes:**
   - Line number (e.g., "CW-4-CS-101")
   - Size (NPS in inches, e.g., "4\"")
   - Schedule (e.g., "Sch 40")
   - Material (e.g., "Carbon Steel A106-B")
   - Service (e.g., "Cooling Water")
   - Approximate length in feet (use scale if visible)

3. **Fittings:**
   - Type (90° elbow, tee, reducer, etc.)
   - Size
   - Material
   - Quantity

4. **Valves:**
   - Type (gate, globe, ball, check, etc.)
   - Size
   - Pressure class
   - Operator (manual, electric, pneumatic)
   - Material
   - Quantity

5. **Flanges:**
   - Type (WN, SO, blind, etc.)
   - Size
   - Pressure class
   - Material
   - Quantity

Return ONLY valid JSON with this structure:
```json
{
  "drawing": {
    "number": "P-042",
    "title": "Cooling Water Supply",
    "scale": "1:50",
    "revision": "A"
  },
  "pipes": [
    {
      "line_number": "CW-4-CS-101",
      "size": "4\\"",
      "schedule": "Sch 40",
      "material": "Carbon Steel",
      "service": "Cooling Water",
      "length_ft": 125.5,
      "confidence": 0.95
    }
  ],
  "fittings": [
    {
      "type": "90° Elbow",
      "size": "4\\"",
      "material": "Carbon Steel",
      "quantity": 8,
      "confidence": 0.92
    }
  ],
  "valves": [
    {
      "type": "Gate Valve",
      "size": "4\\"",
      "pressure_class": "Class 150",
      "operator": "Manual",
      "material": "Carbon Steel",
      "quantity": 2,
      "confidence": 0.91
    }
  ],
  "flanges": [
    {
      "type": "Weld Neck",
      "size": "4\\"",
      "pressure_class": "Class 150",
      "material": "Carbon Steel",
      "quantity": 4,
      "confidence": 0.89
    }
  ],
  "overall_confidence": 0.92,
  "notes": ["Any observations or uncertainties"]
}
```

**Important:**
- Set confidence >0.90 for clear, unambiguous specs
- Set confidence 0.70-0.90 for readable but uncertain items
- Set confidence <0.70 for unclear or estimated items
- Use null for missing information
- Include notes for anything unclear"""

    try:
        # Call Claude Vision API
        print(f"\n🔍 Analyzing drawing: {Path(image_path).name}")
        print("⏳ Calling Claude Sonnet 4.5 Vision API...")
        
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": image_data,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )
        
        # Extract response
        response_text = message.content[0].text
        
        # Try to parse JSON from response
        # Sometimes the model wraps it in markdown code blocks
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.rfind("```")
            response_text = response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.rfind("```")
            response_text = response_text[json_start:json_end].strip()
        
        result = json.loads(response_text)
        
        print("✅ Extraction complete!\n")
        return result
        
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON response: {e}")
        print(f"Raw response:\n{response_text}")
        return None
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        return None

def print_bom(data: dict):
    """Print extracted data as a Bill of Materials"""
    
    print("=" * 80)
    print("EXTRACTED BILL OF MATERIALS")
    print("=" * 80)
    
    # Drawing info
    if "drawing" in data:
        d = data["drawing"]
        print(f"\nDrawing: {d.get('number', 'N/A')} - {d.get('title', 'N/A')}")
        print(f"Scale: {d.get('scale', 'N/A')} | Revision: {d.get('revision', 'N/A')}")
    
    # Pipes
    if "pipes" in data and data["pipes"]:
        print("\n" + "-" * 80)
        print("PIPES")
        print("-" * 80)
        for pipe in data["pipes"]:
            print(f"\nLine: {pipe.get('line_number', 'N/A')}")
            print(f"  Size: {pipe.get('size', 'N/A')} {pipe.get('schedule', 'N/A')}")
            print(f"  Material: {pipe.get('material', 'N/A')}")
            print(f"  Service: {pipe.get('service', 'N/A')}")
            print(f"  Length: {pipe.get('length_ft', 'N/A')} ft")
            print(f"  Confidence: {pipe.get('confidence', 0):.0%}")
    
    # Fittings
    if "fittings" in data and data["fittings"]:
        print("\n" + "-" * 80)
        print("FITTINGS")
        print("-" * 80)
        for fitting in data["fittings"]:
            print(f"\n{fitting.get('quantity', 0)}× {fitting.get('type', 'N/A')}")
            print(f"  Size: {fitting.get('size', 'N/A')}")
            print(f"  Material: {fitting.get('material', 'N/A')}")
            print(f"  Confidence: {fitting.get('confidence', 0):.0%}")
    
    # Valves
    if "valves" in data and data["valves"]:
        print("\n" + "-" * 80)
        print("VALVES")
        print("-" * 80)
        for valve in data["valves"]:
            print(f"\n{valve.get('quantity', 0)}× {valve.get('type', 'N/A')}")
            print(f"  Size: {valve.get('size', 'N/A')} {valve.get('pressure_class', 'N/A')}")
            print(f"  Operator: {valve.get('operator', 'N/A')}")
            print(f"  Material: {valve.get('material', 'N/A')}")
            print(f"  Confidence: {valve.get('confidence', 0):.0%}")
    
    # Flanges
    if "flanges" in data and data["flanges"]:
        print("\n" + "-" * 80)
        print("FLANGES")
        print("-" * 80)
        for flange in data["flanges"]:
            print(f"\n{flange.get('quantity', 0)}× {flange.get('type', 'N/A')}")
            print(f"  Size: {flange.get('size', 'N/A')} {flange.get('pressure_class', 'N/A')}")
            print(f"  Material: {flange.get('material', 'N/A')}")
            print(f"  Confidence: {flange.get('confidence', 0):.0%}")
    
    # Overall
    print("\n" + "=" * 80)
    print(f"Overall Confidence: {data.get('overall_confidence', 0):.0%}")
    if "notes" in data and data["notes"]:
        print("\nNotes:")
        for note in data["notes"]:
            print(f"  • {note}")
    print("=" * 80)

def main():
    """Main entry point"""
    
    # Check for API key
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ Error: ANTHROPIC_API_KEY not found in environment")
        print("Please set it in .env file or export it:")
        print("  export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)
    
    # Check for input file
    if len(sys.argv) < 2:
        print("Usage: python test_vision_poc.py <path_to_image>")
        print("\nSupported formats: .jpg, .jpeg, .png, .gif, .webp")
        print("\nExample:")
        print("  python test_vision_poc.py sample_drawings/P-001.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Extract specs
    result = extract_pipe_specs(image_path)
    
    if result:
        # Print BOM
        print_bom(result)
        
        # Save to JSON file
        output_file = Path(image_path).stem + "_extracted.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
        print(f"\n💾 Results saved to: {output_file}")
    else:
        print("❌ Extraction failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
