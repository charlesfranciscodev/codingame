# Mime Type

This is a solution to the "Mime Type" problem on [Codingame](https://www.codingame.com/training/easy/mime-type).

## Problem Description

You are given a list of file names and their corresponding MIME types. You need to read a list of file names and determine the corresponding MIME type for each file name. If the MIME type cannot be determined, the program should output `UNKNOWN`.

The MIME type is determined by the file extension. The table of file extensions and their corresponding MIME types is given.

| Extension | MIME Type |
|-----------|-----------|
|html       |text/html  |
|htm        |text/html  |
|png        |image/png  |
|jpeg       |image/jpeg |
|jpg        |image/jpeg |
|gif        |image/gif  |
|bmp        |image/bmp  |
|txt        |text/plain|
|pdf        |application/pdf|

The file name may have multiple periods (.) in it, but the extension is always the substring that follows the last period.
