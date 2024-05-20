import re
class Unique:
    def __init__(self):
        self.uniqueList = []
    
    """This will deal with processing files"""
    def processFiles(self, inputSource, outputFile):
        self.uniqueList = self.readItem(inputSource)
        sortedNumbers = self.sort_numbers(self.uniqueList)

        with open(outputFile, 'w') as out:
            for number in sortedNumbers:
                out.write(f"{number}\n")

    """
    This function reads all the unique integers from a given file
    """
    def readItem(self, source):
        uniqueList = []
        with open(source, 'r') as inputSrc:
            for line in inputSrc:
                line = line.strip()
                if self.isValid(line):
                    try:
                        number = int (line)
                        if number not in uniqueList:
                            uniqueList.append(number)
                    except ValueError:
                        continue
        return uniqueList

    """
    This function validates the lines to check if they meet the conditions
    """

    def isValid(self, line):
            # Regex pattern to match lines with punctuation or multiple words
            pattern = re.compile(r'[^\d\s-]|(?<=\S)\s+(?=\S)')
            
            # Check for empty line or if the pattern matches any invalid input
            if line == "" or pattern.search(line):
                return False
            
            # Check if the line is a valid integer
            try:
                int(line)  # This will fail if line is not a valid integer
            except ValueError:
                return False
            
            return True
    
    """ This function will sort the numbers in ascending order. It implements selection sort"""
    def sort_numbers(self, numbers):
        n = len(numbers)
        for i in range(n):
            minIndex = i
            for j in range (i+1, n):
                if numbers[j] < numbers[minIndex]:
                    minIndex = j
            numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
            
        return numbers

if __name__ == "__main__":
    import os

    home_directory = os.path.expanduser("~")
    input_directory = os.path.join(home_directory, "Desktop/dsa/hw01/sample_inputs/")
    output_directory = os.path.join(home_directory, "Desktop/dsa/hw01/sample_results/")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    unique_int = Unique()

    for input_file in os.listdir(input_directory):
        if input_file.endswith(".txt"):
            input_file_path = os.path.join(input_directory, input_file)
            output_file_path = os.path.join(output_directory, f"{input_file}_results.txt")
            unique_int.processFiles(input_file_path, output_file_path)