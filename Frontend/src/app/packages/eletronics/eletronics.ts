export class Eletronics {

  constructor(
    public category: string,
    public big: boolean,
    public fragile: boolean,
    public resistant: boolean,
    public visibility: boolean,
    public heavy: boolean,
    public units: number,
    public length?: number,
    public width?: number,
    public height?: number,
    public budget?: number
  ) {
  }


}
