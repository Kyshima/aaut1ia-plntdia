export class Furniture {

  constructor(
    public category: string,
    public big: boolean,
    public fragile: boolean,
    public pieces: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
}


}
