import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Rommel Chef Master App", page_icon="🍳", layout="wide")

# Style CSS personnalisé
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stCard {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Base de données complète des 39 menus
menus_data = [
    {
        "nom": "1. Spargelcremesuppe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Garde-manger",
        "temps": "Préparation : 15 min | Cuisson : 30 min",
        "ingredients": "• 500g de parures et épluchures d'asperges blanches<br>• 50g d'échalotes ciselées<br>• 40g de beurre<br>• 75cl de bouillon blanc<br>• 20cl de crème liquide entière (Schlagrahm)<br>• Sel, poivre blanc, noix de muscade",
        "etapes": "1. Suer les échalotes et les parures d'asperges dans le beurre sans coloration.<br>2. Mouiller au bouillon blanc, cuire 25 minutes à frémissement.<br>3. Mixer finement, passer au chinois étamine.<br>4. Monter la crème en Schlagrahm et l'incorporer délicatement au moment de l'envoi.",
        "dressage": "Assiette creuse chaude, pointes d'asperges cuites à l'anglais en garniture centrale."
    },
    {
        "nom": "2. Rinderkraftbrühe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 10 min | Cuisson : 15 min",
        "ingredients": "• 1L de bouillon de bœuf clair clarifié<br>• 120g de Flädle (fines crêpes aux herbes taillées en lanières)<br>• Ciboulette fraîche ciselée (10g)",
        "etapes": "1. Réchauffer doucement le bouillon de bœuf clair à frémissement.<br>2. Pocher rapidement les lanières de Flädle dans le bouillon chaud.<br>3. Rectifier l'assaisonnement.",
        "dressage": "Assiette creuse, déposer les Flädle au fond et verser le bouillon bouillant par-dessus, parsemer de ciboulette."
    },
    {
        "nom": "3. Beilagensalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 80g de concombre en rondelles<br>• 70g de carottes râpées<br>• 60g de radis émincés<br>• 100g de salade verte parée<br>• 4cl de vinaigrette maison",
        "etapes": "1. Mariner séparément les crudités avec une fraction de vinaigrette.<br>2. Dresser harmonieusement la salade verte assaisonnée au centre et disposer les crudités autour.",
        "dressage": "Assiette creuse ou coupelle, napper de vinaigrette juste avant l'envoi en salle."
    },
    {
        "nom": "4. Spargel-Erdbeer-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 150g d'asperges blanches cuites<br>• 80g de fraises fraîches tranchées<br>• 140g de filet de sandre (Zander)<br>• 50g de panure anglaise<br>• 4cl de vinaigrette à la framboise<br>• 30g de sauce rémoulade maison",
        "etapes": "1. Paner le filet de sandre et le frire 4 minutes à 180°C.<br>2. Mélanger délicatement les asperges et les fraises avec la vinaigrette framboise.<br>3. Disposer le poisson croustillant à côté.",
        "dressage": "Assiette plate, lit de salade aux fraises et asperges, sandre chaud posé à côté avec une quenelle de rémoulade."
    },
    {
        "nom": "5. Fischknusperle-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 160g de dés de sandre (Zander)<br>• 120g de crudités variées<br>• 80g de salade verte<br>• 40g de sauce rémoulade maison",
        "etapes": "1. Tailler le sandre en dés réguliers, passer en panure anglaise.<br>2. Frire les dés de poisson 3 minutes jusqu'à coloration dorée.<br>3. Mélanger les crudités et la salade avec la vinaigrette.",
        "dressage": "Assiette creuse, mélange de salade au centre, parsemer les croûtes de poisson chaudes."
    },
    {
        "nom": "6. Spargel an Sc. Hollandaise", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 20 min | Cuisson : 15 min",
        "ingredients": "• 400g d'asperges blanches épluchées<br>• 250g de pommes de terre nouvelles<br>• 100g de sauce Hollandaise minute<br>• 20g de beurre",
        "etapes": "1. Cuire les asperges à l'anglais et les pommes de terre à l'eau salée.<br>2. Émulsionner la sauce Hollandaise au bain-marie.<br>3. Égoutter soigneusement.",
        "dressage": "Assiette allongée chaude, asperges au centre nappées de sauce Hollandaise, pommes de terre à côté."
    },
    {
        "nom": "7. Hackbraten", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 20 min | Cuisson : 35 min",
        "ingredients": "• 200g de masse de pain de viande hachée<br>• 100g de champignons de Paris sautés<br>• 12cl de sauce crème (Rahmsoße)<br>• 150g de spätzle au pesto d'ail des ours",
        "etapes": "1. Rôtir le pain de viande au four à 180°C pendant 30 minutes.<br>2. Sauter les champignons minute et lier la sauce crème.<br>3. Réchauffer les spätzle au beurre.",
        "dressage": "Assiette chaude, trancher le hackbraten, napper de sauce aux champignons, accompagner des spätzle."
    },
    {
        "nom": "8. Gegrilltes Lachsfilet", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 10 min | Cuisson : 8 min",
        "ingredients": "• 200g de pavé de saumon frais<br>• 120g d'asperges vertes et blanches<br>• 80g de sauce Hollandaise<br>• 150g de pommes de terre nouvelles",
        "etapes": "1. Cuire les asperges et les pommes de terre.<br>2. Cuire le pavé de saumon côté peau à la poêle (température à cœur ~52°C).<br>3. Napper de sauce Hollandaise.",
        "dressage": "Assiette chaude, lit d'asperges, pavé de saumon grillé par-dessus."
    },
    {
        "nom": "9. Cordon Bleu vom Kalb", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 15 min | Cuisson : 8 min",
        "ingredients": "• 1 escalope de veau de 200g<br>• 40g de jambon<br>• 40g de gruyère corsé<br>• Panure (farine, œuf, chapelure)<br>• 30g de beurre clarifié",
        "etapes": "1. Ouvrir l'escalope, garnir de jambon et fromage, refermer.<br>2. Passer dans la panure anglaise.<br>3. Cuire au beurre clarifié à la poêle.",
        "dressage": "Assiette chaude, Cordon bleu entier, quartier de citron, frites et légumes."
    },
    {
        "nom": "10. Paniertes Schweineschnitzel", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 10 min | Cuisson : 6 min",
        "ingredients": "• 1 escalope de porc de 180g<br>• Panure anglaise complète<br>• 12cl de sauce rôtie (Bratensoße)<br>• 150g de pommes frites",
        "etapes": "1. Aplatir l'escalope et réaliser la panure.<br>2. Cuire en friture jusqu'à dorure.<br>3. Réchauffer la sauce rôtie.",
        "dressage": "Assiette chaude, schnitzel croustillant, frites, sauce rôtie en saucière."
    },
    {
        "nom": "11. Zwiebelrostbraten vom Rinderrücken", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 220g de pavé de dos de bœuf<br>• 150g d'oignons émincés<br>• 15cl de fond de veau brun lié<br>• 30g de beurre clarifié",
        "etapes": "1. Saisir le pavé de bœuf selon la cuisson demandée.<br>2. Confire ou frire les oignons émincés.<br>3. Réchauffer le fond de veau brun.",
        "dressage": "Assiette ronde chaude, pavé nappé de sauce, dôme d'oignons confits, frites."
    },
    {
        "nom": "12. Zanderfilets auf der Haut", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 180g de filet de sandre<br>• 100g de champignons aux herbes<br>• 180g de risotto à l'ail des ours<br>• 20g de beurre",
        "etapes": "1. Cuire le risotto crémeux à l'ail des ours.<br>2. Cuire le filet de sandre unilatéralement sur peau pour le croustillant.",
        "dressage": "Assiette creuse, risotto crémeux au centre, filet de sandre posé sur la peau."
    },
    {
        "nom": "13. Saure Leberle", "resto": "Landgasthof Kreuz", "poste": "Saucier",
        "temps": "Préparation : 10 min | Cuisson : 5 min",
        "ingredients": "• 180g de foie émincé finement<br>• 60g d'oignons émincés<br>• 40g de cornichons au vinaigre<br>• 3cl de vinaigre de vin<br>• 200g de pommes de terre sautées",
        "etapes": "1. Sauter le foie et les oignons à feu vif.<br>2. Déglacer au vinaigre, ajouter les cornichons.",
        "dressage": "Assiette chaude, foie sauté nappé de sa sauce acidulée, pommes de terre sautées."
    },
    {
        "nom": "14. Käsespätzle (hausgemachte)", "resto": "Landgasthof Kreuz", "poste": "Entremet / Pâtes",
        "temps": "Préparation : 25 min | Cuisson : 10 min",
        "ingredients": "• 200g de spätzle frais faits maison<br>• 90g de bio-fromage de montagne de Fontanella<br>• 50g d'oignons rissolés<br>• Persil plat",
        "etapes": "1. Pocher les spätzle dans l'eau bouillante salée.<br>2. Mélanger chaudement avec le fromage râpé pour qu'il file.",
        "dressage": "Assiette creuse chaude, spätzle fondants au fromage, parsemer d'oignons rissolés."
    },
    {
        "nom": "15. Veganes gelbes Kokos-Curry", "resto": "Landgasthof Kreuz", "poste": "Légumier",
        "temps": "Préparation : 20 min | Cuisson : 20 min",
        "ingredients": "• 15cl de lait de coco<br>• 20g de pâte de curry jaune<br>• 100g d'asperges vertes<br>• 120g de légumes de saison grillés<br>• 180g de pommes de terre au four",
        "etapes": "1. Rissoler les légumes, lier avec la pâte de curry et le lait de coco.<br>2. Mijoter 15 minutes.",
        "dressage": "Assiette creuse, curry de légumes onctueux, pommes de terre rôties."
    },
    {
        "nom": "16. Cremiges Spargel-Risotto", "resto": "Landgasthof Kreuz", "poste": "Entremet",
        "temps": "Préparation : 10 min | Cuisson : 20 min",
        "ingredients": "• 100g de riz Arborio<br>• 40cl de bouillon de légumes<br>• 100g d'asperges vertes et blanches<br>• 30g de fromage à pâte dure<br>• 20g de beurre",
        "etapes": "1. Nacrer le riz, mouiller progressivement au bouillon.<br>2. Crémer au beurre et au fromage.",
        "dressage": "Assiette creuse plate, risotto étalé, pointes d'asperges en décor."
    },
    {
        "nom": "17. Wurstsalat (Klassisch)", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g de saucisse de Lyon en lanières<br>• 50g d'oignons en rondelles<br>• 40g de cornichons<br>• 4cl de vinaigrette huile/vinaigre<br>• Pain frais",
        "etapes": "1. Mélanger la saucisse, les oignons et les cornichons.<br>2. Mariner avec la vinaigrette.",
        "dressage": "Assiette creuse, salade de saucisses marinée, pain frais à part."
    },
    {
        "nom": "18. Schweizer Wurstsalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 120g de saucisse en lanières<br>• 80g de fromage emmental<br>• 50g d'oignons, cornichons, marinade, pain",
        "etapes": "1. Mélanger la charcuterie et le fromage avec la marinade.",
        "dressage": "Assiette creuse, mélange lanières saucisse/fromage, oignons, pain."
    },
    {
        "nom": "19. Vegetarischer Käsesalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g de fromage en lamelles<br>• 50g d'oignons, cornichons<br>• Vinaigrette huile/vinaigre<br>• Pain",
        "etapes": "1. Mariner le fromage en lamelles avec les oignons et la vinaigrette.",
        "dressage": "Assiette creuse, fromage mariné, pain ou pommes sautées."
    },
    {
        "nom": "20. Kindergerichte : 'Micky Maus'", "resto": "Landgasthof Kreuz", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g de spätzle frais<br>• 5cl de sauce à la crème douce",
        "etapes": "1. Pocher rapidement les spätzle et lier à la crème.",
        "dressage": "Petite assiette adaptée pour enfant."
    },
    {
        "nom": "21. Kindergerichte : 'Biene Maja'", "resto": "Landgasthof Kreuz", "poste": "Friture",
        "temps": "Cuisson : 4 min",
        "ingredients": "• 120g de frites fraîches<br>• 20g de ketchup",
        "etapes": "1. Frire les frites à 180°C jusqu'à dorure.",
        "dressage": "Petite assiette, frites dorées, ramequin de ketchup."
    },
    {
        "nom": "22. Kindergerichte : 'Pumuckl'", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Cuisson : 6 min",
        "ingredients": "• 100g de petite escalope panée<br>• 100g de frites<br>• 50g de crudités",
        "etapes": "1. Cuire l'escalope et les frites, dresser avec les crudités.",
        "dressage": "Assiette enfant, schnitzel, frites et crudités."
    },
    {
        "nom": "23. Apfelstrudel", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Cuisson : 12 min",
        "ingredients": "• 1 part de strudel aux pommes<br>• 1 boule de glace vanille<br>• 30g de chantilly",
        "etapes": "1. Réchauffer le strudel au four à 180°C (10-12 min).",
        "dressage": "Assiette à dessert, strudel chaud, boule de glace vanille, chantilly."
    },
    {
        "nom": "24. Nuss-Krokant-Becher", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie / Glacier",
        "temps": "Préparation : 5 min",
        "ingredients": "• 2 boules de glace noisette<br>• 20g de krocant<br>• 20g de noix caramélisées<br>• Sirop d'érable, chantilly",
        "etapes": "1. Dresser la coupe à froid minute.",
        "dressage": "Coupe à glace, boules, krocant, noix, chantilly."
    },
    {
        "nom": "25. Mini Dessert : Crème brûlée", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Préparation : 5 min",
        "ingredients": "• 1 ramequin de crème brûlée<br>• 10g de sucre roux",
        "etapes": "1. Saupoudrer de sucre roux et caraméliser au chalumeau.",
        "dressage": "Ramequin sur petite assiette avec cuillère."
    },
    {
        "nom": "26. Erdbeer-Rhabarber-Ragout", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Préparation : 10 min",
        "ingredients": "• 100g de compotée fraise-rhubarbe<br>• 60g de crème mascarpone<br>• 30g de crumble avoine/beurre<br>• 1 boule de glace vanille",
        "etapes": "1. Disposer la compotée, la mascarpone, le crumble et la glace.",
        "dressage": "Assiette creuse, superposition harmonieuse des textures."
    },

    # --- Hof Höfen ---
    {
        "nom": "27. Pommes terre & légumes truffe", "resto": "Hof Höfen", "poste": "Garde-manger / Friture",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 180g de quartiers de pommes de terre<br>• 30g de roquette<br>• 40g de mayonnaise végane à la truffe",
        "etapes": "1. Frire les pommes de terre. Servir avec la roquette et la mayo.",
        "dressage": "Assiette creuse, pommes de terre croustillantes, roquette dessus."
    },
    {
        "nom": "28. Légumes véganes au four", "resto": "Hof Höfen", "poste": "Légumier",
        "temps": "Cuisson : 25 min",
        "ingredients": "• 220g de légumes racines (panais, carottes, betteraves, pommes de terre)<br>• 50g de houmous à l'ail<br>• 10g de graines grillées",
        "etapes": "1. Rôtir au four à 180°C. Servir avec le houmous.",
        "dressage": "Assiette plate, légumes rôtis chauds, houmous, graines."
    },
    {
        "nom": "29. Spätzle au fromage Hof Höfen", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 8 min",
        "ingredients": "• 220g de spätzle maison<br>• 80g de mélange fromage de montagne et Emmental<br>• 40g d'oignons rissolés",
        "etapes": "1. Mélanger les spätzle chauds avec les fromages pour faire filer.",
        "dressage": "Poêlon ou assiette creuse chaude, oignons rissolés par-dessus."
    },
    {
        "nom": "30. Saucisses sauvages de Rommel", "resto": "Hof Höfen", "poste": "Grill / Saucier",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 1 paire de saucisses de gibier (180g)<br>• 200g de salade de pommes de terre",
        "etapes": "1. Cuire à la plancha ou poêle douce pour garder le jus.",
        "dressage": "Assiette rectangulaire, saucisses en diagonale, salade tiède."
    },
    {
        "nom": "31. Escalope de porc panée", "resto": "Hof Höfen", "poste": "Friture / Saucier",
        "temps": "Cuisson : 6 min",
        "ingredients": "• 180g d'escalope panée<br>• 150g de frites ou pommes de terre<br>• 10cl de sauce",
        "etapes": "1. Cuire le schnitzel et l'accompagnement.",
        "dressage": "Assiette chaude, schnitzel croustillant, pommes de terre, sauce."
    },
    {
        "nom": "32. Poitrine de porc rôtie", "resto": "Hof Höfen", "poste": "Saucier / Rôti",
        "temps": "Cuisson : 45 min",
        "ingredients": "• 220g de poitrine de porc<br>• 12cl de jus corsé<br>• 200g de salade de pommes de terre",
        "etapes": "1. Rôtir lentement au four, finir au grill pour croustiller la couenne.",
        "dressage": "Tranche généreuse de poitrine, jus, salade de pommes de terre."
    },
    {
        "nom": "33. Ragoût de venaison braisée", "resto": "Hof Höfen", "poste": "Saucier / Mijotés",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 200g de ragoût de sanglier/chevreuil en sauce<br>• 180g de spätzle maison<br>• 30g de canneberges",
        "etapes": "1. Réchauffer le ragoût, sauter les spätzle au beurre.",
        "dressage": "Assiette creuse, spätzle au fond, ragoût nappé, cuillère de canneberges."
    },
    {
        "nom": "34. Salade de saucisses badoise", "resto": "Hof Höfen", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g de saucisse de Lyon en lamelles, oignons, vinaigrette, 150g de frites",
        "etapes": "1. Assembler la salade badoise et cuire les frites.",
        "dressage": "Assiette creuse, salade marinée, frites croustillantes à côté."
    },
    {
        "nom": "35. Salade Bodanrück", "resto": "Hof Höfen", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 150g de jeunes pousses, carottes, radis, betteraves crues, concombre, tomates, graines",
        "etapes": "1. Mélanger la salade avec la vinaigrette maison.",
        "dressage": "Grand bol de salade colorée, option choisie sur le dessus."
    },
    {
        "nom": "36. Kaiserschmarrn Bodanrück", "resto": "Hof Höfen", "poste": "Pâtisserie / Entremet",
        "temps": "Cuisson : 12 min",
        "ingredients": "• 200g de pâte à crêpe épaisse pochée/déchirée, sucre, compote de pommes",
        "etapes": "1. Caraméliser les morceaux au beurre et sucre à la poêle.",
        "dressage": "Grand plat, morceaux saupoudrés de sucre glace, compote à part."
    },
    {
        "nom": "37. Crème de la forêt de Baden", "resto": "Hof Höfen", "poste": "Pâtisserie",
        "temps": "Préparation : 5 min",
        "ingredients": "• 120g de crème au miel infusée romarin/thym, sirop de miel, physalis",
        "etapes": "1. Dresser la crème fraîchement sortie du froid.",
        "dressage": "Verrine, dôme de crème au miel, filet de sirop de forêt et physalis."
    },
    {
        "nom": "38. Spätzle enfants (sauce)", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g de spätzle, 4cl de sauce",
        "etapes": "1. Pocher et napper de sauce.",
        "dressage": "Petite assiette adaptée."
    },
    {
        "nom": "39. Spätzle enfants (fromage)", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g de spätzle, 40g de fromage",
        "etapes": "1. Mélanger chaudement.",
        "dressage": "Petite assiette creuse."
    }
]

# --- Interface utilisateur ---
st.sidebar.title("🍳 Master Chef Rommel")
st.sidebar.markdown("---")
mode = st.sidebar.radio("Navigation :", ["📖 Fiches Techniques Pro (39 Menus)", "🧠 Quiz d'Entraînement"])

if mode == "📖 Fiches Techniques Pro (39 Menus)":
    st.title("📖 Cahier des 39 Fiches Techniques Professionnelles")
    st.write("Toutes les fiches de poste de cuisine avec ingrédients en grammes, temps et étapes.")

    col1, col2 = st.columns(2)
    with col1:
        f_resto = st.selectbox("Filtrer par Restaurant :", ["Tous", "Landgasthof Kreuz", "Hof Höfen"])
    with col2:
        postes_possibles = ["Tous"] + list(set([m['poste'] for m in menus_data]))
        f_poste = st.selectbox("Filtrer par Poste :", postes_possibles)

    plats_filtres = menus_data
    if f_resto != "Tous":
        plats_filtres = [p for p in plats_filtres if p['resto'] == f_resto]
    if f_poste != "Tous":
        plats_filtres = [p for p in plats_filtres if p['poste'] == f_poste]

    st.markdown(f"Affichage de **{len(plats_filtres)}** fiche(s) technique(s)")

    for plat in plats_filtres:
        st.markdown(f"""
            <div class="stCard">
                <h3>{plat['nom']}</h3>
                <p><b>Restaurant :</b> {plat['resto']} &nbsp;|&nbsp; <b>Poste :</b> <code>{plat['poste']}</code> &nbsp;|&nbsp; ⏱️ <em>{plat['temps']}</em></p>
                <hr style="border-color: #30363d;">
                <p><b>🧪 Ingrédients & Mesures (Grammes) :</b><br>{plat['ingredients']}</p>
                <p><b>🔥 Étapes de Préparation & Cuisson :</b><br>{plat['etapes']}</p>
                <p><b>🍽️ Dressage Standard :</b> {plat['dressage']}</p>
            </div>
        """, unsafe_allow_html=True)

elif mode == "🧠 Quiz d'Entraînement":
    st.title("🧠 Mode Quiz - Révision par Cœur des 39 Menus")
    if 'quiz_item' not in st.session_state:
        st.session_state.quiz_item = random.choice(menus_data)
        st.session_state.reveal = False

    item = st.session_state.quiz_item
    st.info(f"Poste concerné : **{item['poste']}** ({item['resto']})")
    st.write(f"**Préparation / Indice :** {item['etapes'][:120]}...")

    if not st.session_state.reveal:
        if st.button("Afficher la fiche technique complète"):
            st.session_state.reveal = True
            st.rerun()
    else:
        st.success(f"🎯 **Nom exact du plat : {item['nom']}**")
        ingredients_nettoyes = item['ingredients'].replace('<br>', '\n')
        st.write(f"**Ingrédients & Mesures :**\n{ingredients_nettoyes}")
        st.write(f"**Dressage :** {item['dressage']}")
        
        if st.button("Plat Suivant ➡️"):
            st.session_state.quiz_item = random.choice(menus_data)
            st.session_state.reveal = False
            st.rerun()