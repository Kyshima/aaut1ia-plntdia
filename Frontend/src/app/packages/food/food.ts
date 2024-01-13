export class Food {

  constructor(
    public category: string,
    public big: boolean,
    public liquid: boolean,
    public fragile: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
  }


}
