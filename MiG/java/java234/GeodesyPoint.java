import java.lang.Math;


public class GeodesyPoint extends Point{
    
    double measurement_error = 0;
//Point determination error - is a number from 0.01 to 1.00
   
    String anchorage = "none";
 /* 
The pinning method is a string that can contain one of three values:
    long-term boundary mark;
    temporary boundary mark;
    there is no fixing;
*/
    
    String define_method = "none";
/*
Point determination method is a string that can contain one of six values:
    Analytical method;
    Cartometric method;
    Geodetic method;
    Photogrammetric method;
    Method of satellite geodetic measurements;
    Another descriptio
*/

    public GeodesyPoint (double x, double y) {
        super(x, y);
    }

    public GeodesyPoint (GeodesyPoint gp) {
        super(gp.x, gp.y);
        this.measurement_error = gp.measurement_error;
        this.anchorage = gp.anchorage;
        this.define_method = gp.define_method;
    }

    public void setMeasurement_error (double measurement_error) {
        if (measurement_error >= 0.01 && measurement_error <= 1.00) {
            this.measurement_error = measurement_error;
        }
    }

    public void setAnchorage (String anchorage) {
        String[] choices = {"permanent boundary mark", "temporary boundary mark", "no anchorage",};
        for (String anchorageVal: choices) {
            if (anchorage == anchorageVal) {
                this.anchorage = anchorageVal;
            }
        }
    }

    public void setDefine_method (String define_method) {
        String[] choices = {
            "analytical method",
            "cartometric method",
            "geodetic method",
            "photogrammetric method",
            "method of satellite geodetic measurements",
        };

        boolean define_methodIsValid = false;
        for (String defineMethodVal: choices) {
            if (define_method == defineMethodVal) {
                define_methodIsValid = true;
            }
        }

        if (define_methodIsValid) {
            this.define_method = define_method;
        } else {
            this.define_method = "different description";
        }
    }
    public GeodesyPoint incrementPointCoordinates (double xIncrement, double yIncrement) {
        GeodesyPoint incrementedGeodesyPoint = new GeodesyPoint(this);
        incrementedGeodesyPoint.x = incrementedGeodesyPoint.x + xIncrement;
        incrementedGeodesyPoint.y = incrementedGeodesyPoint.y + yIncrement;
        return incrementedGeodesyPoint;
    }

    public GeodesyPoint mirrorRelativeX () {
        GeodesyPoint mirroredGeodesyPoint = new GeodesyPoint(this);
        mirroredGeodesyPoint.y = mirroredGeodesyPoint.y * (-1);
        return mirroredGeodesyPoint;
    }

    public GeodesyPoint mirrorRelativeY () {
        GeodesyPoint mirroredGeodesyPoint = new GeodesyPoint(this);
        mirroredGeodesyPoint.x = mirroredGeodesyPoint.x * (-1);
        return mirroredGeodesyPoint;
    }

    public GeodesyPoint turnPointRelatively (GeodesyPoint gp, double angleMultiplier) {
        double defaultAngle = 90;
        double turnAngle = defaultAngle * angleMultiplier;
        double newX = gp.x + Math.cos(turnAngle)*(this.x - gp.x) - (this.y - gp.y)*Math.sin(turnAngle);
        double newY = gp.y + (this.x - gp.x)*Math.sin(turnAngle) + (this.y - gp.y)*Math.cos(turnAngle);
        GeodesyPoint turnedGeodesyPoint = new GeodesyPoint(this);
        turnedGeodesyPoint.x = newX;
        turnedGeodesyPoint.y = newY;
        return turnedGeodesyPoint;
    }
    
    public GeodesyPoint turnPoint (double angleMultiplier) {
        double defaultAngle = 90;
        double turnAngle = defaultAngle * angleMultiplier;
        double newX = this.x * Math.cos(turnAngle) - this.y * Math.sin(turnAngle);
        double newY = this.x * Math.sin(turnAngle) + this.y * Math.cos(turnAngle);
        GeodesyPoint turnedGeodesyPoint = new GeodesyPoint(this);
        turnedGeodesyPoint.x = newX;
        turnedGeodesyPoint.y = newY;
        return turnedGeodesyPoint;
    }
}

