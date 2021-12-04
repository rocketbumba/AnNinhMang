import pyshark
capture = pyshark.LiveCapture(output_file="pyshark.pcap")
capture.sniff(timeout=10)
