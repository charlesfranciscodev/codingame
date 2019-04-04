import System.IO
import Control.Monad
import Text.Printf
import Data.Char
import Data.List
import Numeric

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  text <- getLine
  let binaryText = toBinary text
  let unaryText = toUnary binaryText
  putStrLn unaryText
  return ()

toBinary :: String -> String
toBinary text = concatMap (printf "%07b") text

firstBlock :: Char -> String
firstBlock x = if x == '0' then "00 " else "0 "

secondBlock :: String -> String
secondBlock l = concatMap show (take (length l) (repeat 0)) ++ " "

toUnary :: String -> String
toUnary text = init (concatMap (\l@(x:xs) -> (firstBlock x) ++ (secondBlock l)) (group text))
