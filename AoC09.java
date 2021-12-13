import java.util.ArrayList;
import java.util.Collections;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class AoC09 {
	
	private static int xmax;
	private static int ymax;
	private static int[][] myArray;
	private static int basinSize;
	
	private static String readFile(String pathString) {
		
		Path filePath = Paths.get(pathString);
		try {
			return Files.readString(filePath);
		}
		catch (IOException e) {
			System.out.println("file not found");
		}
		return "";
	}

	private static void fillArray(String myString) {
	
		String myLines[] = myString.split("\\r?\\n");
		ymax = myLines.length;
		xmax = myLines[0].length();
		myArray = new int[ymax][xmax];
		
		for (int y = 0; y < ymax; y++) {
			for (int x = 0; x < xmax; x++) {
				
				myArray[y][x] = Integer.parseInt(String.valueOf(myLines[y].charAt(x)));
			}
		}
	}

	private static void findTotalRiskLevel() {
	
		int totalRiskLevel = 0;
		
		for (int y = 0; y < ymax; y++) {
			for (int x = 0; x < xmax; x++) {
				
				boolean isLow = true;
				int h = myArray[y][x];
				
				if (isLow && x > 0 && h >= myArray[y][x-1]) {
					isLow = false;
				}
				if (isLow && x < xmax-1 && h >= myArray[y][x+1]) {
					isLow = false;
				}
				if (isLow && y > 0 && h >= myArray[y-1][x]) {
					isLow = false;
				}
				if (isLow && y < ymax-1 && h >= myArray[y+1][x]) {
					isLow = false;
				}
				if (isLow) {
					totalRiskLevel += h + 1;
					//System.out.println("Lowpoint " + h);
				}
			}
		}
		System.out.println("Total risk level: " + totalRiskLevel);
	}

	private static void fillBasins() {
		
		ArrayList<Integer> basinSizeList = new ArrayList<Integer>();
		
		for (int y = 0; y < ymax; y++) {
			for (int x = 0; x < xmax; x++) {
				if (myArray[y][x] < 9) {
					
					basinSize = 0;
					floodFillBasin(x, y);
					basinSizeList.add(basinSize);
					//System.out.println("Basin of size " + basinSize);
				}
			}
		}
		Collections.sort(basinSizeList, Collections.reverseOrder());
		int sizeProduct = 1;
		for (int i = 0; i < 3; i++) {
			//System.out.println("Basin: " + basinSizeList.get(i));
			sizeProduct *= basinSizeList.get(i);
		}
		System.out.println("Basin size product: " + sizeProduct);
	}
	
	private static void floodFillBasin(int x, int y) {
		
		if (x >= 0 && x < xmax &&
			y >= 0 && y < ymax &&
			myArray[y][x] < 9) {
			
			myArray[y][x] = 9;
			basinSize += 1;
			floodFillBasin(x - 1, y);
			floodFillBasin(x + 1, y);
			floodFillBasin(x, y - 1);
			floodFillBasin(x, y + 1);
		}
	}

	public static void main(String[] args) {
		
		String myExample = """
		2199943210
		3987894921
		9856789892
		8767896789
		9899965678
		""";
		
		String myInput = readFile("input\\input09.txt");
		fillArray(myInput);
		findTotalRiskLevel();
		fillBasins();
	}
}