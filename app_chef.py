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

# --- Sélecteur de langue dans la barre latérale ---
st.sidebar.title("🍳 Master Chef Rommel")
langue = st.sidebar.selectbox("🌐 Langue / Sprache :", ["Français", "Deutsch"])
st.sidebar.markdown("---")
mode = st.sidebar.radio("Navigation :", ["📖 Fiches Techniques Pro" if langue == "Français" else "📖 Technische Fächer", "🧠 Quiz d'Entraînement" if langue == "Français" else "🧠 Quiz-Training"])

# Dictionnaires de traduction des éléments d'interface
ui = {
    "Français": {
        "titre_fiches": "📖 Cahier des 39 Fiches Techniques Professionnelles",
        "sous_titre": "Toutes les fiches de poste de cuisine avec ingrédients en grammes, temps et étapes.",
        "filtre_resto": "Filtrer par Restaurant :",
        "filtre_poste": "Filtrer par Poste :",
        "tous": "Tous",
        "affichage": "Affichage de",
        "fiches": "fiche(s) technique(s)",
        " ingredients": "🧪 Ingrédients & Mesures (Grammes) :",
        "etapes": "🔥 Étapes de Préparation & Cuisson :",
        "dressage": "🍽️ Dressage Standard :",
        "titre_quiz": "🧠 Mode Quiz - Révision par Cœur des 39 Menus",
        "indice": "Préparation / Indice :",
        "btn_voir": "Afficher la fiche technique complète",
        "btn_suivant": "Plat Suivant ➡️",
        "nom_plat": "Nom exact du plat :"
    },
    "Deutsch": {
        "titre_fiches": "📖 Technische Rezepturen & Posten-Karten",
        "sous_titre": "Alle Küchen-Fächer mit genauen Gramm-Angaben, Zeiten und Schritten.",
        "filtre_resto": "Nach Restaurant filtern:",
        "filtre_poste": "Nach Posten filtern:",
        "tous": "Alle",
        "affichage": "Anzeige von",
        "fiches": "Technische Karte(n)",
        " ingredients": "🧪 Zutaten & Maße (Gramm) :",
        "etapes": "🔥 Zubereitung & Garprozess :",
        "dressage": "🍽️ Standard-Anrichten :",
        "titre_quiz": "🧠 Quiz-Modus - Herz-Lernen der 39 Menüs",
        "indice": "Vorbereitung / Hinweis :",
        "btn_voir": "Vollständige Rezeptur anzeigen",
        "btn_suivant": "Nächstes Gericht ➡️",
        "nom_plat": "Exakter Name des Gerichts :"
    }
}[langue]

# Base de données complète des 39 menus
menus_data = [
    # --- Landgasthof Kreuz ---
    {
        "nom": "1. Spargelcremesuppe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Garde-manger",
        "temps": "Préparation : 15 min | Cuisson : 30 min",
        "ingredients": "• 500g parures d'asperges blanches<br>• 50g échalotes ciselées<br>• 40g beurre | 75cl bouillon blanc<br>• 20cl crème liquide (Schlagrahm)",
        "etapes": "1. Suer les échalotes et parures dans le beurre.<br>2. Mouiller au bouillon, cuire 25 min.<br>3. Mixer et passer au chinois.<br>4. Incorporer le Schlagrahm au moment.",
        "dressage": "Assiette creuse, pointes d'asperges cuites à l'anglais."
    },
    {
        "nom": "2. Rinderkraftbrühe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 10 min | Cuisson : 15 min",
        "ingredients": "• 1L bouillon de bœuf clarifié<br>• 120g Flädle (crêpes aux herbes)<br>• 10g ciboulette",
        "etapes": "1. Réchauffer le bouillon à frémissement.<br>2. Pocher rapidement les lanières de Flädle.",
        "dressage": "Assiette creuse, Flädle, bouillon bouillant, ciboulette."
    },
    {
        "nom": "3. Beilagensalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 80g concombre | 70g carottes<br>• 60g radis | 100g salade verte<br>• 4cl vinaigrette",
        "etapes": "1. Mariner les crudités.<br>2. Dresser la salade assaisonnée au centre et disposer les crudités autour.",
        "dressage": "Coupelle, napper de vinaigrette."
    },
    {
        "nom": "4. Spargel-Erdbeer-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 150g asperges cuites | 80g fraises<br>• 140g filet de sandre pané<br>• 4cl vinaigrette framboise | 30g rémoulade",
        "etapes": "1. Frire le sandre 4 min à 180°C.<br>2. Mélanger asperges et fraises avec la vinaigrette.",
        "dressage": "Lit de salade fraises/asperges, sandre chaud et quenelle de rémoulade."
    },
    {
        "nom": "5. Fischknusperle-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 160g dés de sandre panés<br>• 120g crudités | 80g salade verte<br>• 40g sauce rémoulade",
        "etapes": "1. Frire les dés de sandre 3 min.<br>2. Mélanger les crudités avec la vinaigrette.",
        "dressage": "Assiette creuse, salade au centre, parsemer de croûtes de poisson."
    },
    {
        "nom": "6. Spargel an Sc. Hollandaise", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 20 min | Cuisson : 15 min",
        "ingredients": "• 400g asperges blanches<br>• 250g pommes de terre nouvelles<br>• 100g sauce Hollandaise | 20g beurre",
        "etapes": "1. Cuire asperges et pommes de terre.<br>2. Émulsionner la Hollandaise au bain-marie.",
        "dressage": "Assiette allongée, asperges nappées de Hollandaise, pommes de terre."
    },
    {
        "nom": "7. Hackbraten", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 20 min | Cuisson : 35 min",
        "ingredients": "• 200g pain de viande hachée<br>• 100g champignons sautés<br>• 12cl sauce crème (Rahmsoße)<br>• 150g spätzle au pesto",
        "etapes": "1. Rôtir le pain de viande au four à 180°C (30 min).<br>2. Sauter les champignons et lier la sauce.",
        "dressage": "Trancher le hackbraten, napper de sauce, accompagner des spätzle."
    },
    {
        "nom": "8. Gegrilltes Lachsfilet", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 10 min | Cuisson : 8 min",
        "ingredients": "• 200g pavé de saumon<br>• 120g asperges vertes/blanches<br>• 80g sauce Hollandaise | 150g pommes de terre",
        "etapes": "1. Cuire le saumon côté peau (à cœur ~52°C).<br>2. Napper de sauce Hollandaise.",
        "dressage": "Lit d'asperges, pavé de saumon grillé, napper de Hollandaise."
    },
    {
        "nom": "9. Cordon Bleu vom Kalb", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 15 min | Cuisson : 8 min",
        "ingredients": "• 200g escalope de veau | 40g jambon<br>• 40g gruyère | Panure anglaise<br>• 30g beurre clarifié",
        "etapes": "1. Garnir l'escalope, paner.<br>2. Cuire au beurre clarifié à la poêle (4 min par face).",
        "dressage": "Cordon bleu entier, quartier de citron, frites et légumes."
    },
    {
        "nom": "10. Paniertes Schweineschnitzel", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 10 min | Cuisson : 6 min",
        "ingredients": "• 180g escalope de porc panée<br>• 12cl sauce rôtie (Bratensoße)<br>• 150g frites",
        "etapes": "1. Frire l'escalope panée jusqu'à dorure.<br>2. Réchauffer la sauce rôtie.",
        "dressage": "Schnitzel croustillant, frites, sauce rôtie."
    },
    {
        "nom": "11. Zwiebelrostbraten vom Rinderrücken", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 220g pavé de bœuf | 150g oignons<br>• 15cl fond de veau brun lié<br>• 30g beurre clarifié",
        "etapes": "1. Saisir le bœuf à la poêle.<br>2. Confire ou frire les oignons.",
        "dressage": "Pavé nappé de sauce, dôme d'oignons confits, frites."
    },
    {
        "nom": "12. Zanderfilets auf der Haut", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 180g filet de sandre | 100g champignons<br>• 180g risotto à l'ail des ours<br>• 20g beurre",
        "etapes": "1. Cuire le risotto.<br>2. Cuire le sandre unilatéralement sur peau.",
        "dressage": "Risotto au centre, filet de sandre posé sur la peau."
    },
    {
        "nom": "13. Saure Leberle", "resto": "Landgasthof Kreuz", "poste": "Saucier",
        "temps": "Préparation : 10 min | Cuisson : 5 min",
        "ingredients": "• 180g foie émincé | 60g oignons<br>• 40g cornichons | 3cl vinaigre de vin<br>• 200g pommes sautées",
        "etapes": "1. Sauter le foie et les oignons à feu vif.<br>2. Déglacer au vinaigre, ajouter les cornichons.",
        "dressage": "Foie sauté nappé de sauce acidulée, pommes sautées."
    },
    {
        "nom": "14. Käsespätzle (hausgemachte)", "resto": "Landgasthof Kreuz", "poste": "Entremet / Pâtes",
        "temps": "Préparation : 25 min | Cuisson : 10 min",
        "ingredients": "• 200g spätzle frais | 90g fromage Fontanella<br>• 50g oignons rissolés | Persil",
        "etapes": "1. Pocher les spätzle dans l'eau bouillante.<br>2. Mélanger chaudement avec le fromage.",
        "dressage": "Spätzle fondants, parsemer d'oignons rissolés."
    },
    {
        "nom": "15. Veganes gelbes Kokos-Curry", "resto": "Landgasthof Kreuz", "poste": "Légumier",
        "temps": "Préparation : 20 min | Cuisson : 20 min",
        "ingredients": "• 15cl lait de coco | 20g curry jaune<br>• 100g asperges | 120g légumes<br>• 180g pommes de terre au four",
        "etapes": "1. Rissoler et mijoter dans le curry coco (15 min).<br>2. Cuire les pommes de terre.",
        "dressage": "Curry de légumes onctueux, pommes de terre rôties."
    },
    {
        "nom": "16. Cremiges Spargel-Risotto", "resto": "Landgasthof Kreuz", "poste": "Entremet",
        "temps": "Préparation : 10 min | Cuisson : 20 min",
        "ingredients": "• 100g riz Arborio | 40cl bouillon<br>• 100g asperges | 30g fromage dur<br>• 20g beurre",
        "etapes": "1. Nacrer le riz, mouiller au bouillon.<br>2. Crémer au beurre et fromage.",
        "dressage": "Risotto étalé, pointes d'asperges en décor."
    },
    {
        "nom": "17. Wurstsalat (Klassisch)", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g saucisse de Lyon en lanières<br>• 50g oignons | 40g cornichons<br>• 4cl vinaigrette | Pain",
        "etapes": "1. Mélanger les ingrédients et mariner 10 min.",
        "dressage": "Salade de saucisses marinée, pain frais à part."
    },
    {
        "nom": "18. Schweizer Wurstsalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 120g saucisse | 80g Emmental<br>• 50g oignons | Marinade | Pain",
        "etapes": "1. Mélanger saucisse, fromage et marinade.",
        "dressage": "Mélange lanières saucisse/fromage, oignons, pain."
    },
    {
        "nom": "19. Vegetarischer Käsesalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g fromage en lamelles | Oignons<br>• Cornichons | Vinaigrette | Pain",
        "etapes": "1. Mariner le fromage avec la vinaigrette.",
        "dressage": "Fromage mariné, pain ou pommes sautées."
    },
    {
        "nom": "20. Kindergerichte : 'Micky Maus'", "resto": "Landgasthof Kreuz", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g spätzle frais | 5cl sauce crème",
        "etapes": "1. Pocher les spätzle, lier à la crème.",
        "dressage": "Petite assiette pour enfant."
    },
    {
        "nom": "21. Kindergerichte : 'Biene Maja'", "resto": "Landgasthof Kreuz", "poste": "Friture",
        "temps": "Cuisson : 4 min",
        "ingredients": "• 120g frites fraîches | 20g ketchup",
        "etapes": "1. Frire les frites à 180°C.",
        "dressage": "Frites dorées, ramequin de ketchup."
    },
    {
        "nom": "22. Kindergerichte : 'Pumuckl'", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Cuisson : 6 min",
        "ingredients": "• 100g petite escalope | 100g frites<br>• 50g crudités",
        "etapes": "1. Cuire escalope et frites.",
        "dressage": "Schnitzel, frites et crudités."
    },
    {
        "nom": "23. Apfelstrudel", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Cuisson : 12 min",
        "ingredients": "• 1 part de strudel | 1 boule vanille<br>• 30g chantilly",
        "etapes": "1. Réchauffer le strudel au four à 180°C.",
        "dressage": "Strudel chaud, glace vanille, chantilly."
    },
    {
        "nom": "24. Nuss-Krokant-Becher", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie / Glacier",
        "temps": "Préparation : 5 min",
        "ingredients": "• 2 boules glace noisette | 20g krocant<br>• 20g noix caramélisées | Chantilly",
        "etapes": "1. Dresser la coupe à froid.",
        "dressage": "Coupe à glace, krocant, noix, chantilly."
    },
    {
        "nom": "25. Mini Dessert : Crème brûlée", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Préparation : 5 min",
        "ingredients": "• 1 ramequin crème brûlée | 10g sucre roux",
        "etapes": "1. Caraméliser le sucre au chalumeau.",
        "dressage": "Ramequin sur petite assiette avec cuillère."
    },
    {
        "nom": "26. Erdbeer-Rhabarber-Ragout", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Préparation : 10 min",
        "ingredients": "• 100g compotée | 60g mascarpone<br>• 30g crumble | 1 boule vanille",
        "etapes": "1. Superposer compotée, mascarpone et crumble.",
        "dressage": "Assiette creuse, textures harmonieuses."
    },

    # --- Hof Höfen ---
    {
        "nom": "27. Pommes terre & légumes truffe", "resto": "Hof Höfen", "poste": "Garde-manger / Friture",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 180g pommes de terre | 30g roquette<br>• 40g mayo végane à la truffe",
        "etapes": "1. Frire les pommes de terre.",
        "dressage": "Pommes de terre croustillantes, roquette dessus, mayo à part."
    },
    {
        "nom": "28. Légumes véganes au four", "resto": "Hof Höfen", "poste": "Légumier",
        "temps": "Cuisson : 25 min",
        "ingredients": "• 220g légumes racines | 50g houmous<br>• 10g graines grillées",
        "etapes": "1. Rôtir au four à 180°C.",
        "dressage": "Légumes rôtis chauds, houmous, graines."
    },
    {
        "nom": "29. Spätzle au fromage Hof Höfen", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 8 min",
        "ingredients": "• 220g spätzle maison | 80g fromage<br>• 40g oignons rissolés",
        "etapes": "1. Mélanger les spätzle chauds avec le fromage.",
        "dressage": "Poêlon ou assiette creuse, oignons rissolés par-dessus."
    },
    {
        "nom": "30. Saucisses sauvages de Rommel", "resto": "Hof Höfen", "poste": "Grill / Saucier",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 1 paire de saucisses de gibier (180g)<br>• 200g salade de pommes de terre",
        "etapes": "1. Cuire à la plancha ou poêle douce.",
        "dressage": "Assiette rectangulaire, saucisses en diagonale, salade tiède."
    },
    {
        "nom": "31. Escalope de porc panée", "resto": "Hof Höfen", "poste": "Friture / Saucier",
        "temps": "Cuisson : 6 min",
        "ingredients": "• 180g escalope panée | 150g frites<br>• 10cl sauce",
        "etapes": "1. Cuire l'escalope et l'accompagnement.",
        "dressage": "Schnitzel croustillant, frites, sauce."
    },
    {
        "nom": "32. Poitrine de porc rôtie", "resto": "Hof Höfen", "poste": "Saucier / Rôti",
        "temps": "Cuisson : 45 min",
        "ingredients": "• 220g poitrine de porc | 12cl jus corsé<br>• 200g salade de pommes de terre",
        "etapes": "1. Rôtir lentement, finir au grill pour la couenne.",
        "dressage": "Tranche de poitrine croustillante, jus, salade."
    },
    {
        "nom": "33. Ragoût de venaison braisée", "resto": "Hof Höfen", "poste": "Saucier / Mijotés",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 200g ragoût de gibier | 180g spätzle<br>• 30g canneberges",
        "etapes": "1. Réchauffer le ragoût, sauter les spätzle.",
        "dressage": "Spätzle au fond, ragoût nappé, cuillère de canneberges."
    },
    {
        "nom": "34. Salade de saucisses badoise", "resto": "Hof Höfen", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g saucisse, oignons, vinaigrette<br>• 150g frites",
        "etapes": "1. Assembler la salade et cuire les frites.",
        "dressage": "Salade marinée, frites croustillantes à côté."
    },
    {
        "nom": "35. Salade Bodanrück", "resto": "Hof Höfen", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 150g jeunes pousses, crudités, graines",
        "etapes": "1. Mélanger la salade avec la vinaigrette.",
        "dressage": "Grand bol de salade colorée."
    },
    {
        "nom": "36. Kaiserschmarrn Bodanrück", "resto": "Hof Höfen", "poste": "Pâtisserie / Entremet",
        "temps": "Cuisson : 12 min",
        "ingredients": "• 200g pâte à crêpe épaisse pochée<br>• Sucre, compote de pommes",
        "etapes": "1. Caraméliser les morceaux au beurre et sucre.",
        "dressage": "Morceaux saupoudrés de sucre glace, compote à part."
    },
    {
        "nom": "37. Crème de la forêt de Baden", "resto": "Hof Höfen", "poste": "Pâtisserie",
        "temps": "Préparation : 5 min",
        "ingredients": "• 120g crème au miel (romarin/thym)<br>• Sirop de miel, physalis",
        "etapes": "1. Sortir du froid et dresser.",
        "dressage": "Verrine, dôme de crème, filet de sirop, physalis."
    },
    {
        "nom": "38. Spätzle enfants (sauce)", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g spätzle | 4cl sauce",
        "etapes": "1. Pocher et napper de sauce.",
        "dressage": "Petite assiette adaptée."
    },
    {
        "nom": "39. Spätzle enfants (fromage)", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 100g spätzle | 40g fromage",
        "etapes": "1. Mélanger chaudement.",
        "dressage": "Petite assiette creuse."
    }
]

# --- Logique d'affichage ---
if mode.startswith("📖"):
    st.title(ui["titre_fiches"])
    st.write(ui["sous_titre"])

    col1, col2 = st.columns(2)
    with col1:
        f_resto = st.selectbox(ui["filtre_resto"], [ui["tous"], "Landgasthof Kreuz", "Hof Höfen"])
    with col2:
        postes_possibles = [ui["tous"]] + list(set([m['poste'] for m in menus_data]))
        f_poste = st.selectbox(ui["filtre_poste"], postes_possibles)

    plats_filtres = menus_data
    if f_resto != ui["tous"]:
        plats_filtres = [p for p in plats_filtres if p['resto'] == f_resto]
    if f_poste != ui["tous"]:
        plats_filtres = [p for p in plats_filtres if p['poste'] == f_poste]

    st.markdown(f"{ui['affichage']} **{len(plats_filtres)}** {ui['fiches']}")

    for plat in plats_filtres:
        st.markdown(f"""
            <div class="stCard">
                <h3>{plat['nom']}</h3>
                <p><b>Restaurant :</b> {plat['resto']} &nbsp;|&nbsp; <b>Poste :</b> <code>{plat['poste']}</code> &nbsp;|&nbsp; ⏱️ <em>{plat['temps']}</em></p>
                <hr style="border-color: #30363d;">
                <p><b>{ui[' ingredients']}</b><br>{plat['ingredients']}</p>
                <p><b>{ui['etapes']}</b><br>{plat['etapes']}</p>
                <p><b>{ui['dressage']}</b> {plat['dressage']}</p>
            </div>
        """, unsafe_allow_html=True)

else:
    st.title(ui["titre_quiz"])
    if 'quiz_item' not in st.session_state:
        st.session_state.quiz_item = random.choice(menus_data)
        st.session_state.reveal = False

    item = st.session_state.quiz_item
    st.info(f"Poste : **{item['poste']}** ({item['resto']})")
    st.write(f"**{ui['indice']}** {item['etapes'][:120]}...")

    if not st.session_state.reveal:
        if st.button(ui["btn_voir"]):
            st.session_state.reveal = True
            st.rerun()
    else:
        st.success(f"🎯 **{ui['nom_plat']} {item['nom']}**")
        ingredients_nettoyes = item['ingredients'].replace('<br>', '\n')
        st.write(f"**Ingrédients :**\n{ingredients_nettoyes}")
        st.write(f"**Dressage :** {item['dressage']}")
        
        if st.button(ui["btn_suivant"]):
            st.session_state.quiz_item = random.choice(menus_data)
            st.session_state.reveal = False
            st.rerun()
