import System.IO
import Control.Monad
import Data.List

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let original = read input_line :: Int
  input_line <- getLine
  let lineNumber = read input_line :: Int
  
  let sequence = conwaySequence [original] lineNumber
  
  putStrLn . intercalate " " $ map show sequence
  return ()

conwaySequence :: [Int] -> Int -> [Int]
conwaySequence xs 1 = xs
conwaySequence xs lineNumber = conwaySequence (nextSequence xs) (lineNumber - 1)

nextSequence :: [Int] -> [Int]
nextSequence xs = concat . map nextNumbers $ group xs

nextNumbers :: [Int] -> [Int]
nextNumbers l@(x:xs) = [(length l)] ++ [x]
