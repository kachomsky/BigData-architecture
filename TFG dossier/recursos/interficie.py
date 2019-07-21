from pyspark.sql import SparkSession

class Localitzacio:
        """
        Classe encarregada de representar una localitzacio i de mapejar la localitzacio amb el seu fitxer .xlsx
        params:
            init: constructor de la classe.  
        """
        def __init__(self, num_loc):
            """
            num_loc: numero de la localitzacio que es vol utilitzar. 
                     1. SANT_FELIU
                     2. CASTELLVI_ROSANES
                     3. SANTA_COLOMA
            """
            self.num_loc = num_loc
            self.SANT_FELIU = 1
            self.CASTELLVI_ROSANES = 2
            self.SANTA_COLOMA = 3
            self.fitxer_dades = self.loc_to_file()

        def loc_to_file(self):
            """
            Funcio encarregada de mapejar cada localitzacio amb el seu corresponent fitxer de dades
            """
            file_map = {
                self.SANT_FELIU : "Base_links_SFLL_Definitiva.csv",
                self.CASTELLVI_ROSANES : "Base_CastellviRosanes.csv",
                self.SANTA_COLOMA : "Base_SantaColomaCervello.csv"
            }
            return file_map[self.num_loc]

class Spark_data:
    """
    Classe que conte totes les funcions necesaries per treballar amb les dades en spark.
    """
    def __init__(self, localitzacio):#cambiar fichero por localizacion para tener los
        self.hdfs_data_location = "hdfs:///user/root/dadesLocalitzacions2/"
        self.localitzacio = localitzacio
        self.fitxer_dades = localitzacio.fitxer_dades
        self.spark_session = SparkSession.builder.appName("Interficie de dades 1").getOrCreate()
        self.spark_df = self.spark_session.read.format("csv").option("header", "true").option("sep",";").option("inferSchema","true").option("encoding", "UTF-8") \
        .load(self.hdfs_data_location + self.fitxer_dades)

    def seleccionar_dades_principals(self):
        if self.localitzacio.num_loc == self.localitzacio.SANT_FELIU:
            return self.spark_df.select("Noms_harmo", "cognom1_harmo", "cognom2_harmo", "DNI", "estat_civil", "parentesc", "ocupacio", "data_naix", "edat")  
        elif self.localitzacio.num_loc == self.localitzacio.CASTELLVI_ROSANES:
            return self.spark_df.select("Persona_nom", "Persona_cognom1", "Persona_cognom2", "Padro_any", "DNI", "Persona_estatcivil", "Persona_parentesc", "Persona_ofici", "Persona_sexe", "Persona_data_naix", "Persona_edata")
        elif self.localitzacio.num_loc == self.localitzacio.SANTA_COLOMA:
            return self.spark_df.select("Persona_nom", "Persona_cognom1", "Persona_cognom2", "Padro_any", "DNI", "Persona_estatcivil", "Persona_parentesc", "Persona_ofici", "Persona_sexe", "Persona_data_naix", "Persona_edata")
        else:
            return "Localitzacio no valida"
    def totes_les_dades(self):
        return self.spark_df

if __name__ == "__main__":
    #Seleccionem la localitzacio de SANT_FELIU
    localitzacio1 = Localitzacio(1)
    localitzacio2 = Localitzacio(2)
    localitzacio3 = Localitzacio(3)
    #Creem un spark data per a gestionar les dades de la localitzacio
    spark_data1 = Spark_data(localitzacio1)
    spark_data2 = Spark_data(localitzacio2)
    spark_data3 = Spark_data(localitzacio3)
    print("El esquema es:")
    spark_data1.spark_df.printSchema()
    spark_data2.spark_df.printSchema()
    spark_data3.spark_df.printSchema()
    print("fin del esquema")
    print(spark_data1.seleccionar_dades_principals())
    print(spark_data2.seleccionar_dades_principals())
    print(spark_data3.seleccionar_dades_principals())