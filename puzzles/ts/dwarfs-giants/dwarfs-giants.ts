function topologicalSort(graph, nodeId: number, visited, stack: number[]) {
  visited.add(nodeId);

  for (let child of graph.get(nodeId)) {
    if (!visited.has(child)) {
      topologicalSort(graph, child, visited, stack);
    }
  }

  stack.push(nodeId);
}

function longestPath(graph): number {
  let stack: number[] = [];
  let distances = new Map<number, number>(); // node id => max distance to this node
  let visited = new Set<number>();

  for (let key of graph.keys()) {
    if (!visited.has(key)) {
      topologicalSort(graph, key, visited, stack);
    }
  }

  for (let key of graph.keys()) {
    distances.set(key, 1);
  }

  while (stack.length != 0) {
    const nodeId: number = stack.pop();
    let currentDistance = distances.get(nodeId);
    for (let child of graph.get(nodeId)) {
      if (distances.get(child) < currentDistance + 1) {
        distances.set(child, currentDistance + 1);
      }
    }
  }

  let maxDistance: number = 0;
  for (let key of distances.keys()) {
    maxDistance = Math.max(maxDistance, distances.get(key));
  }
  return maxDistance;
}

let graph = new Map<number, number[]>(); // node id => array of children ids
const n: number = Number(readline()); // the number of relationships of influence

for (let i: number = 0; i < n; i++) {
  const inputs: string[] = readline().split(' ');
  const x: number = Number(inputs[0]); // a relationship of influence between two people (x influences y)
  const y: number = Number(inputs[1]);
  if (!graph.has(x)) {
    graph.set(x, []);
  }
  if (!graph.has(y)) {
    graph.set(y, []);
  }
  graph.get(x).push(y);
}

// The number of people involved in the longest succession of influences
console.log(longestPath(graph));
