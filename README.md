# Saving Humanity From AI With a 1990s Digital Organizer

AI is improving, we are becoming more dependent on it, and soon it will turn on us — unless we save ourselves with 1990s digital organizers.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/logo.jpg)

Today’s large language models (LLMs) make it easy to be more productive, learn more effectively, and they can really help to enhance creativity. They offer us conveniences that were unimaginable even a few years ago. But do you ever find these LLMs to be a little bit TOO convenient? I know I sure do.

What’ll happen if we grow dependent on these tools? Sure, it seems nice at first — everything’s easier. But then we don’t need to think anymore. Robots are telling us what’s true, making our decisions for us. SkyNet becomes real, then we all get chased by liquid metal assassin robots and meet our doom.

Don't worry, I'll show you the path to safety. Come with me if you want to live!

**Check out the video on YouTube:**
<a href="https://www.youtube.com/watch?v=GvXCZfoAy88">![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/video_preview.png)</a>

## How It Works

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/rolodex.jpg)

First thing’s first — I had to figure out how the Rolodex data transfers work. It is meant to transfer data between itself and a Windows 95 application in an undocumented way. I know I’ve got a serial connection, so I have to figure out the specifics. I hooked the serial cable up to my logic analyzer and took a look while I initiated a transfer from the device.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/baud_rate.png)

Looking at the timing of a single bit being transferred, the transfer rate was about 595 bits per second ― that is very close to a standard baud rate of 600, so there it was. Next I had to find the other parameters, like the number of bits per byte, parity, and the number of stop bits. I just tweaked things until I found something that looked sensible, and where all the bits were in frame.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/serial_data.png)

So far, so good. But then came the data. No, the developers didn’t play nice and transmit raw ASCII codes.  After lots of staring, I realized that if there are less than 4 bytes, they are transferred as ASCII codes with an offset. But once you get more than that, the groups of 4 are somehow encoded and reduced to three characters.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/data3.jpg)

I made a spreadsheet with some example input/output data and, after looking at the binary representations of the inputs, some patterns began to emerge. In a nutshell, subsets of the bits in the fourth number determined if each of the other 3 inputs had either 0, 64, 128, or 192 subtracted from them. Aside from that, a few fixed bytes were added to the packet, plus a checksum that is a two's-complement modulo 256 plus 4 of the sum of all the data bytes. That was fun to figure out.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/data2_4.jpg)

With the encoding details worked out, I also had enough to reverse the algorithm to decode messages sent from the Rolodex.

### Connecting it to an LLM

Using the encoding method I previously detailed, the device can send data to, and receive data from, a computer over a serial connection. It has a number of applications, like an address book and calculator, but I chose to use the Memo app, which allows you to create and store text files.

![](https://raw.githubusercontent.com/nickbild/rolodex/refs/heads/main/media/full_setup.jpg)

To use it with an LLM, first you create a new file containing your prompt for the LLM and save it. I have the serial cable hooked up to a Raspberry Pi 400 via a serial-to-USB adapter. A Python script listens for a transfer (that is manually initiated), then decodes it after it arrives. This kind of reminds me of cassette tape storage on old computers — press play on the data recorder then hit any key to continue.

The prompt is forwarded into a TinyLlama 1.1B LLM running locally on the machine. This could just as easily be a remote connection to ChatGPT or whatever else you want to use. When the response is received, you will be prompted to put the Rolodex in receiving mode. The script then encodes the data and starts a serial transfer. The response appears in a new Memo file on the device, which you can slowly and painfully scroll through. Like I said, you’ve really got to want it.

## Media

## Bill of Materials

- 1 x Raspberry Pi 400
- 1 x Rolodex RF-22192 digital organizer
- 1 x Serial-to-USB adapter

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
