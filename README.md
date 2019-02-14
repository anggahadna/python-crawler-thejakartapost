# Simple Crawler for The Jakarta Post Article

A program that will crawl an article from a page in The Jakarta Post's site and input the article into *.txt file.

--------------

## Getting Started

*Before we start,  I want to tell you that this is just for learning purpose only.*

This simple crawler covers almost all of the articles from The Jakarta Post, except longform and premium content. The program will crawl the title, date, time, and paragraphs from a page and save them into a single *.txt file. The file name will generate itself from the title of the article, but the punctuations will be removed to avoid file naming error.

## Prerequisites

This program uses *BeautifulSoup*, *requests*, and *string* library to run. Make sure you already install them before running the program. Also don't forget to connect your PC to the internet.

## Running the program

Run the program by using

```shell
$ python crawler1_thejakartapost.py
```

When the program asks to input the link, insert the url of the article. Make sure you include the *"https://"* in front of the link, because *requests* library needs it to run. For example, 

```shell
Insert Link (The Jakarta Post) : https://www.thejakartapost.com/life/2019/02/14/singapore-indonesia-associations-sign-mou-on-aerospace-and-astronautics-development.html
```
Then click Enter.

The program will automatically create a .txt file in your directory. In this case, the text file will be :

```
Singapore Indonesia associations sign MoU on aerospace and astronautics development .txt
```

## Note

To make the code simple, this program doesn't accomodate other cases outside the given above. For example, if you insert url without the protocol, it will result an error.

Feel free to give any criticsm and suggesetion. Thanks!
