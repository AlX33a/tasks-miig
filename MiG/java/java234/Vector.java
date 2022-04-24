import java.util.ArrayList;

public class Vector {
    
    private Point start_point;
    private Point end_point;
    private double[] startpoint_coordinates;  //Array of coordinates of the line start point
    private double[] endpoint_coordinates;  //Array of coordinates of the end point of the line
    private double modulo;
    private ArrayList<Double> coordinates = new ArrayList<Double>();  //Array of vector coordinates

    public Vector (Point start_point, Point end_point) {
        this.start_point = start_point;
        this.end_point = end_point;
        this.endpoint_coordinates = this.end_point.get_coordinates();
        this.startpoint_coordinates = this.start_point.get_coordinates();


        for (int i = 0; i < startpoint_coordinates.length; i++) {
            this.modulo += Math.pow(endpoint_coordinates[i] - startpoint_coordinates[i], 2);
        }
        this.modulo = Math.sqrt(modulo);
        //Calculating the modulus of a vector

        for (int i = 0; i < endpoint_coordinates.length; i++) { 
            this.coordinates.add(i, endpoint_coordinates[i] - startpoint_coordinates[i]);
        }
        //Vector coordinates calculation
    }

    public Point get_startpoint() {
        return this.start_point;
    }

    public Point get_endpoint() {
        return this.end_point;
    }

    public ArrayList<Double> get_coordinates() {
        return this.coordinates;
    }

    public double get_modulo() {
        return this.modulo;
    }

    public double scalar_product(Vector vector) {
        double product;
        product = 0;
        for (int i = 0; i < this.coordinates.size(); i++) {
            product += this.coordinates.get(i) * vector.coordinates.get(i);
        }
        return product;
    }

    public double pseudoscalar_product(Vector vector) {
        double product;
        int j = this.coordinates.size() - 1;
        product = this.coordinates.get(0) * vector.coordinates.get(j);
        j--;
        for (int i = 1; i < this.coordinates.size(); i++) {
            product -= this.coordinates.get(i) * vector.coordinates.get(j);
            j--;
        }
        return product;
    }

    public double cosine(Vector vector) {
        double scalarProduct = this.scalar_product(vector);
        double cosine = (this.modulo * vector.modulo) / scalarProduct;
        return cosine;
    }

    public double sine(Vector vector) {
        return this.pseudoscalar_product(vector) / (this.modulo * vector.modulo);
    }
}
