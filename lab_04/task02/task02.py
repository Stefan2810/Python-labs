class Image():

    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels

    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    
    def sepia(self):
        # apply sepia filter to the image
        for i in range(self.rows):
            j=2
            while j <= (3 * self.columns) - 1:
                r=self.pixels[i][j-2]
                g=self.pixels[i][j-1]
                b=self.pixels[i][j] 
                
                self.pixels[i][j-2] = (int)(0.393*r + 0.769*g + 0.189*b)
                self.pixels[i][j-1] = (int)(0.349*r + 0.686*g + 0.168*b)
                self.pixels[i][j] = (int)(0.272*r + 0.534*g + 0.131*b)

                if self.pixels[i][j-2] >= self.max_value :
                    self.pixels[i][j-2]=self.max_value

                if self.pixels[i][j-1] >= self.max_value :
                    self.pixels[i][j-1]=self.max_value

                if self.pixels[i][j] >= self.max_value :
                    self.pixels[i][j]=self.max_value

                j+=3

    def read(self, filename):
        # read from file and assign the correct parameters (see README and input examples)
        with open(filename, "r") as file:
            self.format = file.readline()
            dimensions = list(map(int, file.readline().split()))
            self.rows = dimensions[0]
            self.columns = dimensions[1]
            self.max_value = int(file.readline().strip())
            self.pixels = []
            for line in file:
                values = list(map(int, line.split()))
                self.pixels.append(values)

    def write(self, filename):
        # write to file in the correct format (see README and input examples)
        with open(filename, "w") as file:
            file.write(f"{self.format}{self.rows} {self.columns}\n{self.max_value}\n")
            for i in range(self.rows):
                for j in range( 3 * self.columns):
                    file.write(str(self.pixels[i][j]) + ' ')
                file.write("\n")