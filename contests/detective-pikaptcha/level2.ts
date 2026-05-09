class Pikachu {
  public start: [number, number] = [0, 0];
  public previous: [number, number] = [0, 0];
  public x: number = 0;
  public y: number = 0;
  public facing: string = "";
  public priorities: { [key: string]: string[] } = {};

  public isTrapped(): boolean {
    return this.previous[0] === this.x && this.previous[1] === this.y;
  }
}

class Game {
  private WALL: string = "#";

  private FOLLOW_RIGHT: string = "R";
  private FOLLOW_LEFT: string = "L";

  private RIGHT: string = ">";
  private DOWN: string = "v";
  private LEFT: string = "<";
  private UP: string = "^";

  private DIRECTIONS: string[] = [this.RIGHT, this.DOWN, this.LEFT, this.UP];

  private rows: string[][] = [];
  private width: number = 0;
  private height: number = 0;
  private pika: Pikachu = new Pikachu();

  public readInput(): void {
    const input = readline().split(" ");
    this.width = parseInt(input[0]);
    this.height = parseInt(input[1]);

    for (let y = 0; y < this.height; y++) {
      const line = readline();
      this.rows.push([]);
      for (let x = 0; x < this.width; x++) {
        if (this.DIRECTIONS.includes(line[x])) {
          this.pika.start = [x, y];
          this.pika.x = x;
          this.pika.y = y;
          this.pika.facing = line[x];
        }
        if (line[x] === this.WALL) {
          this.rows[y].push(this.WALL);
        } else {
          this.rows[y].push("0");
        }
      }
    }

    const follow = readline();
    if (follow === this.FOLLOW_RIGHT) {
      this.pika.priorities = {
        [this.UP]: [this.RIGHT, this.UP, this.LEFT, this.DOWN],
        [this.DOWN]: [this.LEFT, this.DOWN, this.RIGHT, this.UP],
        [this.RIGHT]: [this.DOWN, this.RIGHT, this.UP, this.LEFT],
        [this.LEFT]: [this.UP, this.LEFT, this.DOWN, this.RIGHT],
      };
    } else if (follow === this.FOLLOW_LEFT) {
      this.pika.priorities = {
        [this.UP]: [this.LEFT, this.UP, this.RIGHT, this.DOWN],
        [this.DOWN]: [this.RIGHT, this.DOWN, this.LEFT, this.UP],
        [this.RIGHT]: [this.UP, this.RIGHT, this.DOWN, this.LEFT],
        [this.LEFT]: [this.DOWN, this.LEFT, this.UP, this.RIGHT],
      };
    }
  }

  public solve(): void {
    while (!this.isPikachuBackAtTheStart()) {
      const priorityList = this.pika.priorities[this.pika.facing];
      this.pika.previous = [this.pika.x, this.pika.y];

      for (const priority of priorityList) {
        if (priority === this.RIGHT) {
          if (this.pikachuCanGoRight()) {
            this.pika.facing = this.RIGHT;
            this.pika.x += 1;
            break;
          }
        } else if (priority === this.DOWN) {
          if (this.pikachuCanGoDown()) {
            this.pika.facing = this.DOWN;
            this.pika.y += 1;
            break;
          }
        } else if (priority === this.LEFT) {
          if (this.pikachuCanGoLeft()) {
            this.pika.facing = this.LEFT;
            this.pika.x -= 1;
            break;
          }
        } else if (priority === this.UP) {
          if (this.pikachuCanGoUp()) {
            this.pika.facing = this.UP;
            this.pika.y -= 1;
            break;
          }
        }
      }

      if (this.pika.isTrapped()) {
        break;
      }
      this.rows[this.pika.y][this.pika.x] = (
        parseInt(this.rows[this.pika.y][this.pika.x]) + 1
      ).toString();
    }
  }

  public isPikachuBackAtTheStart(): boolean {
    return (
      this.pika.x === this.pika.start[0] &&
      this.pika.y === this.pika.start[1] &&
      this.rows[this.pika.y][this.pika.x] !== "0"
    );
  }

  public pikachuCanGoDown(): boolean {
    return (
      this.pika.y < this.height - 1 &&
      this.rows[this.pika.y + 1][this.pika.x] !== this.WALL
    );
  }

  public pikachuCanGoLeft(): boolean {
    return this.pika.x > 0 && this.rows[this.pika.y][this.pika.x - 1] !== this.WALL;
  }

  public pikachuCanGoRight(): boolean {
    return (
      this.pika.x < this.width - 1 &&
      this.rows[this.pika.y][this.pika.x + 1] !== this.WALL
    );
  }

  public pikachuCanGoUp(): boolean {
    return this.pika.y > 0 && this.rows[this.pika.y - 1][this.pika.x] !== this.WALL;
  }

  public printSolution(): void {
    for (const row of this.rows) {
      console.log(row.join(""));
    }
  }
}

const game = new Game();
game.readInput();
game.solve();
game.printSolution();
