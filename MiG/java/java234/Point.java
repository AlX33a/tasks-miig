public class Point {
    
    public double x;
    public double y;

    public double[] get_coordinates () {
        double[] coordinates = {this.x, this.y};
        return coordinates;
    }

    public Point (double x, double y) {
        this.x = x;
        this.y = y;
    }

}