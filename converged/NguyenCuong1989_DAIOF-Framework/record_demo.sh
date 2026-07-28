#!/bin/bash
# Automated demo recording for DAIOF Framework

echo "🎬 Starting automated demo recording..."

# Record demo.sh execution
asciinema rec assets/demo.cast --overwrite --command "./demo.sh"

echo ""
echo "✅ Recording complete: assets/demo.cast"
echo ""
echo "To convert to GIF, install agg:"
echo "  cargo install --git https://github.com/asciinema/agg"
echo "  agg assets/demo.cast assets/demo.gif"
echo ""
echo "Or view online:"
echo "  asciinema play assets/demo.cast"
