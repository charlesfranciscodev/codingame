import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
    public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

let n = Int(readLine()!)! // the number of temperatures to analyse
var minTemperature = 5526

for i in ((readLine()!).split(separator: " ").map(String.init)) {
    let temperature = Int(i)!
    if (abs(temperature) < abs(minTemperature)) || (abs(temperature) == abs(minTemperature) && temperature > minTemperature) {
        minTemperature = temperature
    }
}

if n == 0 {
    print(0)
} else {
    print(minTemperature)
}