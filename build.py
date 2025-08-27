#!/usr/bin/env python3
"""
Build script for Involute Sans font project.
This script generates TTF, WOFF, and WOFF2 fonts from source OTF files.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

# Try to import fontTools
try:
    import fontTools
    FONTTools_AVAILABLE = True
except ImportError:
    FONTTools_AVAILABLE = False

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {cmd}")
        print(f"   Error: {e.stderr}")
        return False

def create_directories():
    """Create necessary directories for the project."""
    directories = [
        "fonts/ttf",
        "fonts/woff", 
        "fonts/woff2",
        "sources"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def convert_glyphs_to_otf():
    """Convert .glyphs file to .otf format using cu2qu."""
    print("🔄 Converting .glyphs to .otf...")
    
    glyphs_file = "InvoluteSans-Regular.glyphs"
    if not os.path.exists(glyphs_file):
        print(f"❌ {glyphs_file} not found")
        return False
        
    try:
        cmd = f"glyphsLib {glyphs_file} sources/InvoluteSans-Regular.ufo"
        if not run_command(cmd, "Converting .glyphs to .ufo"):
            return False
            
        # Convert UFO to OTF using ufo2ft
        if os.path.exists("sources/InvoluteSans-Regular.ufo"):
            from ufoLib2 import Font
            from ufo2ft import compileCFF
            
            # Load UFO
            ufo = Font.open("sources/InvoluteSans-Regular.ufo")
            
            # Convert to OTF
            otf = compileCFF(ufo)
            
            # Save the OTF file
            output_file = "sources/InvoluteSans-Regular.otf"
            otf.save(output_file)
            
            # Clean up UFO directory
            shutil.rmtree("sources/InvoluteSans-Regular.ufo")
            
            print("✅ Successfully converted .glyphs to .otf")
            return True
        else:
            print("❌ UFO conversion failed")
            return False
            
    except Exception as e:
        print(f"❌ Error converting .glyphs to .otf: {str(e)}")
        return False

def build_fonts():
    """Build TTF, WOFF, and WOFF2 fonts from source OTF files."""
    source_dir = "sources"
    ttf_dir = "fonts/ttf"
    woff_dir = "fonts/woff"
    woff2_dir = "fonts/woff2"
    
    # Check if fonttools is available
    if not FONTTools_AVAILABLE:
        print("❌ fonttools not found. Please install it with: pip install fonttools")
        return False
    
    print("✅ fonttools is available")
    
    # Process each OTF file
    for otf_file in Path(source_dir).glob("*.otf"):
        base_name = otf_file.stem
        
        # Generate TTF using fontforge
        ttf_path = f"{ttf_dir}/{base_name}.ttf"
        ff_script = f'Open($1); Generate($2); Close();'
        cmd = f'echo "{ff_script}" | fontforge -lang=ff -c "Open(\\"{otf_file}\\"); Generate(\\"{ttf_path}\\"); Close();"'
        if not run_command(cmd, f"Generating TTF for {base_name}"):
            continue
        
        # Generate WOFF
        woff_path = f"{woff_dir}/{base_name}.woff"
        cmd = f'fontforge -lang=ff -c "Open(\\"{ttf_path}\\"); Generate(\\"{woff_path}\\"); Close();"'
        if not run_command(cmd, f"Generating WOFF for {base_name}"):
            continue
        
        # Generate WOFF2
        woff2_path = f"{woff2_dir}/{base_name}.woff2"
        cmd = f'fontforge -lang=ff -c "Open(\\"{ttf_path}\\"); Generate(\\"{woff2_path}\\"); Close();"'
        if not run_command(cmd, f"Generating WOFF2 for {base_name}"):
            continue
        
        print(f"🎉 Successfully built all formats for {base_name}")
    
    return True

def validate_fonts():
    """Validate generated font files."""
    print("🔍 Validating font files...")
    
    # Check if files exist
    font_dirs = ["fonts/ttf", "fonts/woff", "fonts/woff2"]
    total_files = 0
    existing_files = 0
    
    for font_dir in font_dirs:
        if os.path.exists(font_dir):
            files = list(Path(font_dir).glob("*.ttf")) + list(Path(font_dir).glob("*.woff")) + list(Path(font_dir).glob("*.woff2"))
            total_files += len(files)
            existing_files += len([f for f in files if f.exists()])
    
    if existing_files > 0:
        print(f"✅ Found {existing_files} font files")
        return True
    else:
        print("❌ No font files found")
        return False

def main():
    """Main build process."""
    print("🚀 Starting Involute Sans font build process...")
    print("=" * 50)
    
    # Create project structure
    create_directories()
    
    # Build fonts directly from OTF
    if not build_fonts():
        print("❌ Font building failed")
        sys.exit(1)
    
    # Validate results
    if not validate_fonts():
        print("❌ Font validation failed")
        sys.exit(1)
    
    print("=" * 50)
    print("🎉 Build process completed successfully!")
    print("\nGenerated fonts:")
    print("  📁 fonts/ttf/     - TrueType fonts")
    print("  📁 fonts/woff/    - WOFF fonts")
    print("  📁 fonts/woff2/   - WOFF2 fonts")
    print("  📁 sources/       - Source OTF files")
    print("\nNext steps:")
    print("  1. Review generated fonts")
    print("  2. Test fonts in web browsers")
    print("  3. Update METADATA.pb if needed")
    print("  4. Commit changes to version control")

if __name__ == "__main__":
    main()
