translations = {
    'en': {
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
        """  # <-- Ensure this closing triple quote is here
    },
    'hu': {
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
        """  # <-- Ensure this closing triple quote is here
    }
}
