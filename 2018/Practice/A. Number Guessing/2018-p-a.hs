-- Offical Sample Solution

import System.IO

getNum :: IO Int
getNum = do
    x <- getLine
    let n = read x :: Int
    return n

bisect :: Int -> Int -> Int -> String -> IO ()
bisect a b m "CORRECT" = return ()
bisect a b m "TOO_SMALL" = singleCase (m+1) b
bisect a b m "TOO_BIG" = singleCase a (m-1)

query :: Int -> IO String
query m = do
    putStrLn ( show m )
    hFlush stdout
    x <- getLine
    return x

singleCase :: Int -> Int -> IO ()
singleCase a b = do
    let m = (a+b) `div` 2
    response <- query m
    bisect a b m response
    return ()

solve :: Int -> IO ()
solve 0 = return ()
solve n = do
    [a, b] <- fmap (map read.words) getLine
    _ <- getNum
    singleCase (a+1) b
    solve (n-1)

main = do
    hSetBuffering stdout NoBuffering
    t <- getNum
    solve t