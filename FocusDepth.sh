
for v in $(seq 1.0 0.5 6.0); do
rpicam-still --lens-position $v --timeout 1000 -o test-$v.jpg
done