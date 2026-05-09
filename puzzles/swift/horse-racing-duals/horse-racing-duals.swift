import Glibc
import Foundation

public struct StderrOutputStream: TextOutputStream {
    public mutating func write(_ string: String) { fputs(string, stderr) }
}
public var errStream = StderrOutputStream()

if let n = readLine(), let nInt = Int(n) {
    var strengths: [Int] = []
    var minDiff = 10000000

    for _ in 0..<nInt {
        if let strengthStr = readLine(), let strength = Int(strengthStr) {
            strengths.append(strength)
        }
    }

    strengths.sort()

    for i in 0..<(nInt - 1) {
        let diff = strengths[i + 1] - strengths[i]
        if diff < minDiff {
            minDiff = diff
        }
    }

    print(minDiff)
}
