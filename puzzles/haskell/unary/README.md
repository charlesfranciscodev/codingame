# Unary

```haskell
import System.IO
import Control.Monad
import Text.Printf
import Data.Char
import Data.List
import Numeric
```

The code above imports necessary modules for input/output operations, control flow, text formatting, character manipulation, list operations, and numeric conversions.

```haskell
main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  text <- getLine
  let binaryText = toBinary text
  let unaryText = toUnary binaryText
  putStrLn unaryText
  return ()
```

The `main` function is the entry point of the program. It reads a line of input from the user using `getLine`. Then, it converts the input text to binary using the `toBinary` function and assigns the result to `binaryText`. Next, it converts the binary text to unary using the `toUnary` function and assigns the result to `unaryText`. Finally, it prints the unary text using `putStrLn`.

```haskell
toBinary :: String -> String
toBinary text = concatMap (printf "%07b") text
```

The `toBinary` function takes a `String` as input and converts each character of the string to its 7-bit binary representation. It achieves this by applying the `printf` function with the format specifier `"%07b"` to each character of the input text using `concatMap`.

```haskell
firstBlock :: Char -> String
firstBlock x = if x == '0' then "00 " else "0 "
```

The `firstBlock` function takes a `Char` as input and returns a string representing the first block of the unary representation for that character. If the input character is `'0'`, it returns `"00 "`; otherwise, it returns `"0 "`.

```haskell
secondBlock :: String -> String
secondBlock l = concatMap show (take (length l) (repeat 0)) ++ " "
```

The `secondBlock` function takes a `String` as input and returns a string representing the second block of the unary representation for that string. It creates a list of zeros with the same length as the input string using `repeat 0`, takes the first `length l` elements from that list using `take`, converts each element to a string using `show`, concatenates the resulting list of strings using `concatMap`, and appends a space at the end.

```haskell
toUnary :: String -> String
toUnary text = init (concatMap (\l@(x:xs) -> (firstBlock x) ++ (secondBlock l)) (group text))
```

The `toUnary` function takes a `String` as input and converts it to its unary representation. It does this by grouping consecutive equal characters using `group`, and then applying a lambda function to each group. The lambda function takes the first character of the group `x` and the rest of the group `xs`, and concatenates the first block of the unary representation of `x` with the second block of the unary representation of the entire group. The resulting unary representations are concatenated using `concatMap`. Finally, the last character (a space) is removed using `init` to form the complete unary representation.
