import java.lang.*;
import java.util.Scanner;

/* Use the following steps to run your java program in the cmd
 * 1) Open cmd
 * 2) Go to the path of the folder where the file of your program is located
 * 3) Use the following command: javac App.java ; java App
 * Note: App.java is the name of the file and will generate the program. java App runs the program that was generated in the previus step
 */

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        // Operations +, -, *, /, %
        // Any operation between different types is going to take the larger type
        cuboid();
    }

    public static void area_of_triangle() {
        float base, height, area;
        System.out.print("Enter base and height: ");

        Scanner sc = new Scanner(System.in);
        base = sc.nextFloat();
        height = sc.nextFloat();

        area = base * height / 2;

        System.out.println("The area of the triangle is: " + area);
    }

    public static void area_of_triangle2() {
        float a, b, c, s;
        double area;
        System.out.print("Give me the values of a, b, c (separated with spaces): ");

        Scanner sc = new Scanner(System.in);
        a = sc.nextFloat();
        b = sc.nextFloat();
        c = sc.nextFloat();

        s = (a + b + c)/2;
        area = Math.sqrt(s * (s - a) * (s - b) * (s - c));

        System.out.println("The area of the triangle is: " + area);
    }

    public static void quadratic_formula() {
        float a, b, c;
        double r1, r2;
        System.out.print("Please give me a, b, c: ");

        Scanner sc = new Scanner(System.in);
        a = sc.nextFloat();
        b = sc.nextFloat();
        c = sc.nextFloat();

        r1 = (-b + Math.sqrt(Math.pow(b, 2) - (4 * a * c)))/2 * a;
        r2 = (-b - Math.sqrt(Math.pow(b, 2) - (4 * a * c)))/2 * a;

        System.out.println("The first answer is: " + r1 + " || The second answer is: " + r2);

    }

    public static void cuboid() {
        float length, height, breadth, area, volume;
        System.out.print("Please give me the length, height and breadth: ");

        Scanner sc = new Scanner(System.in);
        length = sc.nextFloat();
        height = sc.nextFloat();
        breadth = sc.nextFloat();

        area = 2 * length * breadth + 2 * length * height + 2 * breadth * height;
        volume = height * length * breadth;

        System.out.println("The area of the cuboid is: " + area + " || The volume of the cuboid is: " + volume);
    }
}
