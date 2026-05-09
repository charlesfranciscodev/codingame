import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
    public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

// game loop
while true {
    let enemy1 = readLine()! // name of enemy 1
    let distance1 = Int(readLine()!)! // distance to enemy 1
    let enemy2 = readLine()! // name of enemy 2
    let distance2 = Int(readLine()!)! // distance to enemy 2

    if distance1 < distance2 {
        print(enemy1)
    } else {
        print(enemy2)
    }
}
