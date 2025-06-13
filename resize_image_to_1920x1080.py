#!/usr/bin/env python3
"""
Script to resize an image to 1920x1080 by adding white space padding
without stretching the original image.

Usage:
    python resize_image_to_1920x1080.py <input_image_path> [--top]
    
Examples:
    python resize_image_to_1920x1080.py "path/to/image.png"
    python resize_image_to_1920x1080.py "path/to/image.jpg" --top
"""

from PIL import Image, ImageOps
import sys
import os
import argparse
from pathlib import Path

def resize_with_padding(input_path, output_path, target_width=1920, target_height=1080, add_padding_to_bottom=True):
    """
    Resize image to target dimensions by adding white padding to either top or bottom.
    
    Args:
        input_path: Path to input image
        output_path: Path to save output image
        target_width: Target width (default 1920)
        target_height: Target height (default 1080)
        add_padding_to_bottom: If True, add padding to bottom; if False, add to top
    """
    
    print("=" * 60)
    print("STARTING IMAGE RESIZE WITH PADDING")
    print("=" * 60)
    
    # Open the original image
    with Image.open(input_path) as img:
        print(f"✓ Successfully opened input image")
        print(f"  Original image size: {img.width} x {img.height} pixels")
        print(f"  Original image mode: {img.mode}")
        print(f"  Target size: {target_width} x {target_height} pixels")
        
        # Calculate the scaling factor to fit within target dimensions
        scale_width = target_width / img.width
        scale_height = target_height / img.height
        scale_factor = min(scale_width, scale_height)
        
        print(f"\n📏 SCALING CALCULATIONS:")
        print(f"  Scale factor for width: {scale_width:.4f}")
        print(f"  Scale factor for height: {scale_height:.4f}")
        print(f"  Using scale factor: {scale_factor:.4f} (smaller to maintain aspect ratio)")
        
        # Calculate new dimensions (maintaining aspect ratio)
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        
        print(f"  Scaled image size: {new_width} x {new_height} pixels")
        
        # Resize the image maintaining aspect ratio
        print(f"\n🔄 Resizing image using LANCZOS resampling...")
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        print(f"✓ Image resized successfully")
        
        # Create a new image with target dimensions and white background
        print(f"\n🎨 Creating canvas with white background...")
        final_img = Image.new('RGBA', (target_width, target_height), (255, 255, 255, 255))
        print(f"✓ Created {target_width}x{target_height} white canvas")
        
        # Calculate position - center horizontally, add padding to top OR bottom
        x_offset = (target_width - new_width) // 2
        
        # Calculate vertical padding
        total_vertical_padding = target_height - new_height
        
        if add_padding_to_bottom:
            y_offset = 0  # Place image at top
            padding_location = "bottom"
        else:
            y_offset = total_vertical_padding  # Place image at bottom
            padding_location = "top"
        
        print(f"\n📐 POSITIONING CALCULATIONS:")
        print(f"  Horizontal centering: x_offset = {x_offset} pixels")
        print(f"  Total vertical padding needed: {total_vertical_padding} pixels")
        print(f"  Adding padding to: {padding_location}")
        print(f"  Vertical position: y_offset = {y_offset} pixels")
        
        # Paste the resized image onto the white background
        print(f"\n🖼️  Pasting resized image onto canvas...")
        final_img.paste(resized_img, (x_offset, y_offset), resized_img if resized_img.mode == 'RGBA' else None)
        print(f"✓ Image pasted at position ({x_offset}, {y_offset})")
        
        # Convert to RGB if needed (for JPEG output)
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            print(f"\n🔄 Converting to RGB for JPEG output...")
            final_img = final_img.convert('RGB')
        
        # Save the final image
        print(f"\n💾 Saving final image...")
        final_img.save(output_path, quality=95)
        print(f"✓ Saved resized image to: {output_path}")
        print(f"✓ Final image size: {target_width} x {target_height} pixels")
        
        print(f"\n🎉 SUCCESS! Image processing complete!")
        print("=" * 60)

def main():
    parser = argparse.ArgumentParser(
        description="Resize an image to 1920x1080 by adding white padding without stretching",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python resize_image_to_1920x1080.py "my-image.png"
  python resize_image_to_1920x1080.py "folder/image.jpg" --top
  python resize_image_to_1920x1080.py "/full/path/to/image.png"

The output file will be saved in the same directory with "-1920x1080" added to the filename.
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the input image file (PNG, JPG, JPEG supported)'
    )
    
    parser.add_argument(
        '--top',
        action='store_true',
        help='Add white padding to the top instead of bottom (default: bottom)'
    )
    
    parser.add_argument(
        '--width',
        type=int,
        default=1920,
        help='Target width in pixels (default: 1920)'
    )
    
    parser.add_argument(
        '--height',
        type=int,
        default=1080,
        help='Target height in pixels (default: 1080)'
    )
    
    args = parser.parse_args()
    
    print("🚀 STARTING IMAGE RESIZE SCRIPT")
    print(f"📅 Current time: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Convert to Path object for easier manipulation
    input_path = Path(args.input_file)
    
    # Generate output filename in the same directory
    output_filename = f"{input_path.stem}-{args.width}x{args.height}{input_path.suffix}"
    output_path = input_path.parent / output_filename
    
    print(f"\n📁 FILE PATHS:")
    print(f"  Input:  {input_path.absolute()}")
    print(f"  Output: {output_path.absolute()}")
    
    if not input_path.exists():
        print(f"\n❌ ERROR: Input file not found!")
        print(f"   Expected: {input_path.absolute()}")
        sys.exit(1)
    
    # Check if it's a supported image format
    supported_formats = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}
    if input_path.suffix.lower() not in supported_formats:
        print(f"\n❌ ERROR: Unsupported file format!")
        print(f"   File: {input_path.suffix}")
        print(f"   Supported: {', '.join(supported_formats)}")
        sys.exit(1)
    
    print(f"✓ Input file exists and format is supported")
    
    try:
        # Add padding to bottom by default, or top if --top flag is used
        add_padding_to_bottom = not args.top
        resize_with_padding(
            str(input_path), 
            str(output_path), 
            target_width=args.width,
            target_height=args.height,
            add_padding_to_bottom=add_padding_to_bottom
        )
        print(f"\n🎊 ALL DONE! Your image has been resized successfully!")
        print(f"📍 Find your new image at: {output_path.absolute()}")
    except ImportError as e:
        print(f"\n❌ ERROR: Missing required library!")
        print(f"   {e}")
        print(f"\n💡 TIP: Install Pillow with: pip install Pillow")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        print(f"\n🔍 FULL ERROR DETAILS:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
