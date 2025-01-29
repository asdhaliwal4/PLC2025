listFunc :: Int -> Int -> [Int]
listFunc a b = [a..b]  

applicatorFunc :: (Int -> Int -> [Int]) -> Int -> Int -> Char -> Float
applicatorFunc inpFunc a b s
    | s == 's'  = fromIntegral (sum (inpFunc a b))  
    | otherwise = fromIntegral (sum (inpFunc a b)) / fromIntegral (length (inpFunc a b))  

main :: IO ()
main = do
    putStrLn "Enter start of range:"
    a <- readLn
    putStrLn "Enter end of range:"
    b <- readLn
    putStrLn "Enter 's' for sum or anything else for average:"
    s <- getLine
    print (applicatorFunc listFunc a b (head s))