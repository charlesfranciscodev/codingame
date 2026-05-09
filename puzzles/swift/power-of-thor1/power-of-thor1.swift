import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
    public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

let inputs = (readLine()!).split(separator: " ").map(String.init)
let lightX = Int(inputs[0])! // the X position of the light of power
let lightY = Int(inputs[1])! // the Y position of the light of power
var thorX = Int(inputs[2])! // Thor's starting X position
var thorY = Int(inputs[3])! // Thor's starting Y position

// game loop
while true {
    var direction = ""
    if thorY > lightY {
        direction += "N"
        thorY -= 1
    } else if thorY < lightY {
        direction += "S"
        thorY += 1
    }
    
    if thorX > lightX {
        direction += "W"
        thorX -= 1
    } else if thorX < lightX {
        direction += "E"
        thorX += 1
    }

    // A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
}
