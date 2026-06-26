#!/bin/bash

echo "Installing DotSpace..."

# Create install location
INSTALL_DIR="$HOME/.dotspace"
mkdir -p "$INSTALL_DIR"

# Copy interpreter
cp dotspace.py "$INSTALL_DIR/"

# Create a launcher command
LAUNCHER="/usr/local/bin/dotspace"

sudo tee "$LAUNCHER" > /dev/null <<EOF
#!/bin/bash
python3 $INSTALL_DIR/dotspace.py "\$@"
EOF

sudo chmod +x "$LAUNCHER"

echo "✅ DotSpace installed!"
echo "Run programs with: dotspace <yourfile.ds>"
