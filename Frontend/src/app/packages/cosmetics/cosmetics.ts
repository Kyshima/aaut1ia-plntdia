export class Cosmetics {

  constructor(
    public category: string,
    public fragile: boolean,
    public liquid: boolean,
    public big: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
  }
}
