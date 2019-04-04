function bfs(graph, gateways, agentNodeId) {
  let visited = new Set();
  let queue = [];
  let cameFrom = new Map();  // node id => parent node id on the shortest path
  queue.push(agentNodeId);
  visited.add(agentNodeId);

  while (queue.length !== 0) {
    nodeId = queue.shift();
    for (let neighborId of graph.get(nodeId)) {
      if (!visited.has(neighborId)) {
        visited.add(neighborId);
        queue.push(neighborId);
        cameFrom.set(neighborId, nodeId);
        if (gateways.has(neighborId)) {
          return [cameFrom, neighborId];
        }
      }
    }
  }

  return [null, null];
}

function reconstructPath(cameFrom, neighborId) {
  let currentId = neighborId;
  let stack = [];

  while (cameFrom.has(currentId)) {
    stack.push(currentId);
    currentId = cameFrom.get(currentId);
  }
  stack.push(currentId);
  return stack;
}


// read game input
let graph = new Map(); // node id => links
let gateways = new Set();
let inputs = readline().split(' ');
const nbNodes = parseInt(inputs[0]); // the total number of nodes in the level, including the gateways
const nbLinks = parseInt(inputs[1]); // the number of links
const nbGateways = parseInt(inputs[2]); // the number of exit gateways
for (let i = 0; i < nbLinks; i++) {
  let inputs = readline().split(' ');
  // n1 and n2 defines a link between these nodes
  const n1 = parseInt(inputs[0]);
  const n2 = parseInt(inputs[1]);
  if (!graph.has(n1)) {
    graph.set(n1, new Set());
  }
  if (!graph.has(n2)) {
    graph.set(n2, new Set());
  }
  graph.get(n1).add(n2);
  graph.get(n2).add(n1);
}
for (let i = 0; i < nbGateways; i++) {
  gateways.add(parseInt(readline()));
}

// game loop
while (true) {
  const agentNodeId = parseInt(readline()); // node id on which the Skynet agent is located
  [cameFrom, neighborId] = bfs(graph, gateways, agentNodeId);
  if (cameFrom !== null && neighborId !== null) {
    path = reconstructPath(cameFrom, neighborId);
    secondNodeId = path[path.length - 2];
    graph.get(agentNodeId).delete(secondNodeId);
    graph.get(secondNodeId).delete(agentNodeId);
  }

  // the indices of the nodes you wish to sever the link between
  console.log(`${agentNodeId} ${secondNodeId}`);
}
