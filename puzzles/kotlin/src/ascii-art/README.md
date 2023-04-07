Sure, here is a modified version of the documentation for `ascii-art.kt` without the license section:

# ASCII Art

ASCII Art is a Kotlin program that takes in a string of characters and outputs a stylized version of the input using ASCII art. The program works by converting the input string into a series of characters and then replacing each character with a corresponding ASCII art representation.

## Usage

To use ASCII Art, you need to provide a string of characters and a font size. The font size specifies the height of the ASCII art characters in rows. Here is an example usage of the program:

```kotlin
fun main() {
    val input = "HELLO"
    val fontSize = 5
    val asciiArt = AsciiArt(input, fontSize)
    println(asciiArt)
}
```

This will output the ASCII art representation of the string "HELLO" with a font size of 5.