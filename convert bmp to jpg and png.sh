#!/bin/bash
for f in *.bmp; do
    convert -quality 100 "$f" "${f%.bmp}.png"
    convert -quality 100 "$f" "${f%.bmp}.jpg"
done
