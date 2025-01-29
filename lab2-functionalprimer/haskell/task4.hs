ask :: String -> IO ()
ask prompt = do
    putStrLn prompt
    line <- getLine
    if line == "quit"
        then putStrLn "quitting..."
        else if line == ""
            then ask (prompt ++ "!")  -- Add an extra "!" each time Enter is pressed
            else do
                putStrLn ("you said: " ++ reverse line)
                ask prompt  -- Keep prompting until "quit" is entered

main :: IO ()
main = do
    let prompt = "please say something"
    ask prompt
