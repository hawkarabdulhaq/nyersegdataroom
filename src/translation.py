translations = {
    'en': {
        # General App Texts
        'page_title': "Nyerseg Dataroom",
        'welcome_message': """
        **Welcome to the Nyerseg Dataroom by Hawkar Ali Abdulhaq, Szeged University**  
        **Contact**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)
        """,
        'access_key_prompt': "Please enter the access key to proceed:",
        'access_key_label': "Access Key",
        'access_button': "Access",
        'access_granted': "Access granted! You may now use the app.",
        'invalid_key': "Invalid access key. Please try again.",
        'navigation': "Navigation",
        'home': "Home",
        'shape_cleaning': "Shape Cleaning",
        'generate_wells': "Generate Wells",
        'clean_wells': "Clean Wells",
        'download': "Download",
        'how_this_app_works': "How This App Works",
        'app_instructions': """
        This app follows a sequential workflow to prepare and visualize well data. Each page offers a specific function, allowing you to process and interact with the data in a logical order. Below is a guide to each page's purpose:
        
        1. **Shape Cleaning**:  
           - This page loads the initial field shapefile and consolidates fields that are close to each other.
           - Adjust the buffer distance, run the cleaning, and see "before and after" comparisons to ensure accuracy.
           
        2. **Generate Wells**:  
           - Based on field size, this page generates virtual wells within each field, placing wells randomly around the centroid of each field.
           - Customize parameters, such as the offset range and number of wells per field size category.
        
        3. **Clean Wells**:  
           - This page filters generated wells to remove any that are too close to each other or real wells, ensuring optimal spacing.
           - Adjust minimum distance criteria and visualize the results on a filtered map.
        
        4. **Download**:  
           - View the final interactive map showing only real and filtered generated wells.
           - Download the map as an HTML file for external sharing or offline viewing.
        
        By following these steps in sequence, you can prepare a clean, well-organized dataset that is ready for visualization and download.
        """,

        # Shape Cleaning Page Texts
        'shape_cleaning_title': "Shape Cleaning - Clean and Merge Shapefiles",
        'shape_cleaning_description': """
        **Objective**: This page runs the cleanshp.py script, which cleans and merges shapefile data by buffering and merging close polygons. 
        The process is useful for consolidating fields that are near each other, simplifying visualization and analysis.
        """,
        'buffer_distance_label': "Select Buffer Distance (meters)",
        'buffer_distance_set': "Buffer distance set to: {} meters",
        'run_clean_button': "Run CleanSHP",
        'processing_message': "Processing... Please wait.",
        'success_message': "Merged shapefile saved to {}",
        'error_message': "An error occurred: {}",
        'original_fields': "Original Fields",
        'merged_fields': "Merged Fields with {} m Buffer",
        'longitude_label': "Longitude",
        'latitude_label': "Latitude",

        # Generate Wells Page Texts
        'generate_wells_title': "Generate Wells",
        'generate_wells_description': """
        **Objective**: This script generates wells within each field based on field area and user-defined parameters. 
        The wells are placed randomly around the center of each field, with the number determined by the field's size.
        """,
        'offset_range_label': "Offset Range from Centroid (meters)",
        'field_area_section': "Set Number of Wells Based on Field Area",
        'small_fields_label': "Number of wells for Small fields (< 5,000 m²)",
        'medium_fields_label': "Number of wells for Medium fields (5,000 - 10,000 m²)",
        'large_fields_label': "Number of wells for Large fields (10,000 - 50,000 m²)",
        'very_large_fields_label': "Number of wells for Very large fields (> 50,000 m²)",
        'generate_wells_button': "Generate Wells",
        'generated_wells_saved': "Generated wells saved to {}",
        'map_saved': "Map has been created and saved as {}",
        'well_locations_title': "Well Locations within Fields",

        # Reduce Wells Page Texts
        'reduce_wells_title': "Reduce Generated Wells",
        'reduce_wells_description': """
        **Objective**: This page filters generated wells based on minimum distance criteria to prevent close clustering. 
        It removes wells that are either too close to other generated wells or within a specified distance from real wells.
        """,
        'min_distance_generated_label': "Minimum Distance Between Generated Wells (meters)",
        'min_distance_real_label': "Minimum Distance from Real Wells (meters)",
        'run_well_reduction_button': "Run Well Reduction",
        'filtered_wells_saved': "Filtered wells saved to {}",
        'filtered_wells_map_saved': "Filtered wells map saved to {}",
        'histogram_saved': "Filtered well distances histogram saved to {}",
        'well_locations_with_filters': "Well Locations with Distance Filters Applied",
        'easting_label': "Easting (meters)",
        'northing_label': "Northing (meters)",
        'histogram_title': "Histogram of Pairwise Well Distances (Filtered)",
        'histogram_x_label': "Distance (meters)",
        'histogram_y_label': "Frequency",

        # Final Map Page Texts
        'final_map_title': "Final Map of Real and Generated Wells",
        'final_map_description': """
        This page displays the final positions of generated wells, filtered to ensure appropriate distances from real wells, 
        alongside the real well locations on an interactive map. The map can also be downloaded as an HTML file.
        Additionally, you can download the generated EOV X and Y coordinates for the filtered generated wells.
        """,
        'real_well_popup': "Real Well {}",
        'generated_well_popup': "Generated Well {}",
        'map_saved_message': "Interactive map saved as HTML at {}",
        'download_map_button': "Download Map as HTML",
        'download_generated_wells_button': "Download Generated Wells EOV Coordinates",
    },
    'hu': {
        # General App Texts
        'page_title': "Nyerseg Adattár",
        'welcome_message': """
        **Üdvözöljük a Nyerseg Adattárban, Hawkar Ali Abdulhaq, Szegedi Egyetem**  
        **Kapcsolat**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)
        """,
        'access_key_prompt': "Kérjük, adja meg a hozzáférési kulcsot a folytatáshoz:",
        'access_key_label': "Hozzáférési kulcs",
        'access_button': "Hozzáférés",
        'access_granted': "Hozzáférés engedélyezve! Most már használhatja az alkalmazást.",
        'invalid_key': "Érvénytelen hozzáférési kulcs. Kérjük, próbálja újra.",
        'navigation': "Navigáció",
        'home': "Kezdőlap",
        'shape_cleaning': "Alak tisztítása",
        'generate_wells': "Kutak generálása",
        'clean_wells': "Kutak tisztítása",
        'download': "Letöltés",
        'how_this_app_works': "Hogyan működik ez az alkalmazás",
        'app_instructions': """
        Ez az alkalmazás egy szekvenciális munkafolyamatot követ a kútadatok előkészítéséhez és megjelenítéséhez. Minden oldal egy specifikus funkciót kínál, lehetővé téve az adatok logikus sorrendben történő feldolgozását és interakcióját. Az alábbiakban egy útmutató található az egyes oldalak céljához:
        
        1. **Alak tisztítása**:  
           - Ez az oldal betölti a kezdeti mező alakfájlt, és egyesíti az egymáshoz közeli mezőket.
           - Állítsa be a puffer távolságot, futtassa a tisztítást, és tekintse meg az "előtte és utána" összehasonlításokat a pontosság biztosítása érdekében.
           
        2. **Kutak generálása**:  
           - A mező mérete alapján ez az oldal virtuális kutakat generál minden mezőben, véletlenszerűen elhelyezve a kutakat minden mező centroidja körül.
           - Testreszabhatja a paramétereket, mint például az eltolási tartományt és a kutak számát mezőméret kategóriánként.
        
        3. **Kutak tisztítása**:  
           - Ez az oldal kiszűri a generált kutakat, hogy eltávolítsa azokat, amelyek túl közel vannak egymáshoz vagy valódi kutakhoz, biztosítva az optimális távolságot.
           - Állítsa be a minimális távolság kritériumait, és tekintse meg az eredményeket egy szűrt térképen.
        
        4. **Letöltés**:  
           - Tekintse meg a végső interaktív térképet, amely csak a valódi és a szűrt generált kutakat mutatja.
           - Töltse le a térképet HTML fájlként külső megosztáshoz vagy offline megtekintéshez.
        
        Ezeknek a lépéseknek a sorrendben történő követésével tiszta, jól szervezett adatállományt készíthet elő, amely készen áll a megjelenítésre és letöltésre.
        """,

        # Shape Cleaning Page Texts
        'shape_cleaning_title': "Alak tisztítása - Alakfájlok tisztítása és egyesítése",
        'shape_cleaning_description': """
        **Cél**: Ez az oldal a cleanshp.py szkriptet futtatja, amely tisztítja és egyesíti az alakfájl adatokat puffereléssel és közeli poligonok egyesítésével.
        Ez a folyamat hasznos a közel álló mezők egyesítésében, egyszerűsítve a megjelenítést és az elemzést.
        """,
        'buffer_distance_label': "Válassza ki a puffer távolságot (méterben)",
        'buffer_distance_set': "A puffer távolság beállítva: {} méter",
        'run_clean_button': "CleanSHP futtatása",
        'processing_message': "Feldolgozás folyamatban... Kérjük, várjon.",
        'success_message': "Az egyesített alakfájl mentve a következő helyre: {}",
        'error_message': "Hiba történt: {}",
        'original_fields': "Eredeti mezők",
        'merged_fields': "Egyesített mezők {} m pufferrel",
        'longitude_label': "Hosszúság",
        'latitude_label': "Szélesség",

        # Generate Wells Page Texts
        'generate_wells_title': "Kutak generálása",
        'generate_wells_description': """
        **Cél**: Ez a szkript kutakat generál minden mezőben, a mező mérete és a felhasználó által meghatározott paraméterek alapján. 
        A kutakat véletlenszerűen helyezi el a mező központja körül, a mező mérete alapján meghatározott számban.
        """,
        'offset_range_label': "Eltolási tartomány a centrumból (méterben)",
        'field_area_section': "Állítsa be a kutak számát a mező területe alapján",
        'small_fields_label': "Kutak száma kis mezők esetén (< 5,000 m²)",
        'medium_fields_label': "Kutak száma közepes mezők esetén (5,000 - 10,000 m²)",
        'large_fields_label': "Kutak száma nagy mezők esetén (10,000 - 50,000 m²)",
        'very_large_fields_label': "Kutak száma nagyon nagy mezők esetén (> 50,000 m²)",
        'generate_wells_button': "Kutak generálása",
        'generated_wells_saved': "A generált kutak mentve a következő helyre: {}",
        'map_saved': "A térkép elkészült és elmentve a következő helyre: {}",
        'well_locations_title': "Kútelhelyezések a mezőkben",

        # Reduce Wells Page Texts
        'reduce_wells_title': "Generált kutak csökkentése",
        'reduce_wells_description': """
        **Cél**: Ez az oldal minimális távolsági kritériumok alapján szűri a generált kutakat, hogy megakadályozza a szoros halmozódást.
        Eltávolítja azokat a kutakat, amelyek túl közel vannak más generált kutakhoz vagy egy meghatározott távolságon belül esnek valódi kutakhoz.
        """,
        'min_distance_generated_label': "Minimális távolság a generált kutak között (méterben)",
        'min_distance_real_label': "Minimális távolság a valódi kutaktól (méterben)",
        'run_well_reduction_button': "Kútcsökkentés futtatása",
        'filtered_wells_saved': "Szűrt kutak mentve a következő helyre: {}",
        'filtered_wells_map_saved': "A szűrt kutak térképe mentve a következő helyre: {}",
        'histogram_saved': "A szűrt kutak távolsági hisztogramja mentve a következő helyre: {}",
        'well_locations_with_filters': "Kútelhelyezések távolsági szűrőkkel",
        'easting_label': "Keleti (méter)",
        'northing_label': "Északi (méter)",
        'histogram_title': "Párosított kúttávolságok hisztogramja (szűrt)",
        'histogram_x_label': "Távolság (méter)",
        'histogram_y_label': "Gyakoriság",

        # Final Map Page Texts
        'final_map_title': "A valódi és generált kutak végső térképe",
        'final_map_description': """
        Ez az oldal megjeleníti a generált kutak végső pozícióit, amelyek a valódi kutaktól való megfelelő távolság biztosítása érdekében lettek szűrve, 
        valamint a valódi kutak helyeit egy interaktív térképen. A térkép HTML fájlként is letölthető.
        Továbbá letöltheti a generált EOV X és Y koordinátákat a szűrt generált kutakhoz.
        """,
        'real_well_popup': "Valódi kút {}",
        'generated_well_popup': "Generált kút {}",
        'map_saved_message': "Az interaktív térkép HTML-ként mentve a következő helyre: {}",
        'download_map_button': "Térkép letöltése HTML formátumban",
        'download_generated_wells_button': "Generált kutak EOV koordinátáinak letöltése",
    }
}
