# pcaptomsc

converting wireshark packet capture (pcap) into message sequence chart for sequencediagram.net, hackmd.io, or mscgen (png, svg, and eps format).

## Requirements
- wireshark
- python 3.3
- mscgen (optional, for convering to image files)

## Usage
- `python pcaptomsc.py -f <format> -i <pcap_file_input> -o <text_file_output>`

	the method above will result specified format msc displayed in terminal and saved in the text_file_output

	supported output text format:
	- sequencediagram.net
	- hackmd
	- mscgen

- `python pcaptomsc.py -i <pcap_file_input>`

	the method above will result hackmd formatted msc displayed in terminal

- `python pcaptomsc.py -f mscgen -i <pcap_file_input> -o <image_file_output>`

	the method above will result specified format msc displayed in terminal, msc file output, and image file.

	supoported image format (based on mscgen):
	- png
	- eps
	- svg

- `python pcaptomsc.py -f mscgen -i <pcap_file_input> -o <text_file_output> -o <image_file_output>`

	the method above will result specified format msc displayed in terminal, text file output, msc file output, and image file.
	
## License
This project is licensed under MIT. Contributions to this project are accepted under the same license.
