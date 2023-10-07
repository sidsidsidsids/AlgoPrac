function solution(maps) {
  const Y = maps.length;
  const X = maps[0].length;
  let sL, lL, eL;

  for (let y = 0; y < Y; y++) {
    for (let x = 0; x < X; x++) {
      if (maps[y][x] === 'S') {
        sL = [y, x];
      } else if (maps[y][x] === 'L') {
        lL = [y, x];
      } else if (maps[y][x] === 'E') {
        eL = [y, x];
      }
    }
  }

  let able = false;
  const Q = [];
  Q.push(sL);
  const V = Array.from({ length: Y }, () => Array(X).fill(0));
  V[sL[0]][sL[1]] = 1;
  let lDist = 0;

  while (Q.length > 0) {
    const elems = Q.shift();
    const i = elems[0];
    const j = elems[1];

    const directions = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]];

    for (const [ni, nj] of directions) {
      if (0 <= ni && ni < Y && 0 <= nj && nj < X && maps[ni][nj] !== 'X') {
        if (!V[ni][nj]) {
          if (maps[ni][nj] === 'L') {
            lDist = V[i][j] + 1;
            break;
          } else {
            V[ni][nj] = V[i][j] + 1;
            Q.push([ni, nj]);
          }
        }
      }
    }

    if (lDist) {
      lDist -= 1;
      able = true;
      break;
    }
  }
  let eDist = 0;
  if (able) {
    able = false;
    Q.length = 0;
    Q.push(lL);
    const V = Array.from({ length: Y }, () => Array(X).fill(0));
    V[lL[0]][lL[1]] = 1;
    

    while (Q.length > 0) {
      const elems = Q.shift();
      const i = elems[0];
      const j = elems[1];

      const directions = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]];

      for (const [ni, nj] of directions) {
        if (0 <= ni && ni < Y && 0 <= nj && nj < X && maps[ni][nj] !== 'X') {
          if (!V[ni][nj]) {
            if (maps[ni][nj] === 'E') {
              eDist = V[i][j] + 1;
              break;
            } else {
              V[ni][nj] = V[i][j] + 1;
              Q.push([ni, nj]);
            }
          }
        }
      }

      if (eDist) {
        eDist -= 1;
        able = true;
        break;
      }
    }
  }

  if (able) {
    return lDist + eDist;
  } else {
    return -1;
  }
}
