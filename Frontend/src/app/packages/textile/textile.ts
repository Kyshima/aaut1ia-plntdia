export class Textile {

  constructor(
    public category: string,
    public delicate: boolean,
    public big: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
  }
}
