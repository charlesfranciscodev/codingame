# Mime Type

This is a Kotlin solution to the "Mime Type" problem on [Codingame](https://www.codingame.com/training/easy/mime-type).

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

## Solution

The solution reads the number of file names, the number of MIME types and the list of file name and MIME type pairs. It stores the MIME types in a map with the extension as the key. Then it reads a list of file names and determines the corresponding MIME type by looking up the extension in the map. If the extension is not found, it outputs `UNKNOWN`.

## Usage

To use the solution, copy the code in the [mime-type.kt](https://github.com/charlesfranciscodev/codingame/blob/master/puzzles/kotlin/src/mime-type.kt) file and run it in a Kotlin environment. The input is read from the standard input and the output is written to the standard output.

## Example

Input:

```
2
4
html text/html
png image/png
gif image/gif
txt text/plain
file.html
file.txt
```

Output:

```
text/html
text/plain
```

## Code

```kotlin
import java.util.*

fun main(args : Array<String>) {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextInt()
    val q = scanner.nextInt()
    val map = mutableMapOf<String, String>()
    for (i in 0 until q) {
        val ext = scanner.next()
        val mime = scanner.next()
        map[ext.toLowerCase()] = mime
    }
    for (i in 0 until n) {
        val fileName = scanner.next()
        val extension = fileName.substringAfterLast('.').toLowerCase()
        val mime = map[extension]
        println(mime ?: "UNKNOWN")
    }
}
```

