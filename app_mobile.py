import flet as ft
import random

# Base de données complète des 39 menus
menus_data = [
    # --- Landgasthof Kreuz ---
    {
        "nom": "1. Spargelcremesuppe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Garde-manger",
        "temps": "Préparation : 15 min | Cuisson : 30 min",
        "ingredients": "• 500g parures d'asperges blanches\n• 50g échalotes ciselées\n• 40g beurre | 75cl bouillon blanc\n• 20cl crème liquide (Schlagrahm)",
        "etapes": "1. Suer les échalotes et parures dans le beurre.\n2. Mouiller au bouillon, cuire 25 min.\n3. Mixer et passer au chinois.\n4. Incorporer le Schlagrahm au moment.",
        "dressage": "Assiette creuse, pointes d'asperges cuites à l'anglais."
    },
    {
        "nom": "2. Rinderkraftbrühe", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 10 min | Cuisson : 15 min",
        "ingredients": "• 1L bouillon de bœuf clair clarifié\n• 120g Flädle (crêpes aux herbes)\n• 10g ciboulette fraîche",
        "etapes": "1. Réchauffer le bouillon à frémissement.\n2. Pocher rapidement les lanières de Flädle.",
        "dressage": "Assiette creuse, Flädle au fond, verser le bouillon bouillant, parsemer de ciboulette."
    },
    {
        "nom": "3. Beilagensalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 80g concombre | 70g carottes\n• 60g radis | 100g salade verte\n• 4cl vinaigrette maison",
        "etapes": "1. Mariner les crudités.\n2. Dresser la salade assaisonnée au centre et disposer les crudités autour.",
        "dressage": "Coupelle, napper de vinaigrette juste avant l'envoi."
    },
    {
        "nom": "4. Spargel-Erdbeer-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 150g asperges cuites | 80g fraises\n• 140g filet de sandre pané\n• 4cl vinaigrette framboise | 30g rémoulade",
        "etapes": "1. Frire le sandre 4 min à 180°C.\n2. Mélanger asperges et fraises avec la vinaigrette.",
        "dressage": "Assiette plate, lit de salade fraises/asperges, sandre chaud et quenelle de rémoulade."
    },
    {
        "nom": "5. Fischknusperle-Salat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger / Poisson",
        "temps": "Préparation : 15 min | Cuisson : 5 min",
        "ingredients": "• 160g dés de sandre panés\n• 120g crudités | 80g salade verte\n• 40g sauce rémoulade",
        "etapes": "1. Frire les dés de sandre 3 min.\n2. Mélanger les crudités avec la vinaigrette.",
        "dressage": "Assiette creuse, salade au centre, parsemer de croûtes de poisson."
    },
    {
        "nom": "6. Spargel an Sc. Hollandaise", "resto": "Landgasthof Kreuz", "poste": "Entremet / Saucier",
        "temps": "Préparation : 20 min | Cuisson : 15 min",
        "ingredients": "• 400g asperges blanches\n• 250g pommes de terre nouvelles\n• 100g sauce Hollandaise | 20g beurre",
        "etapes": "1. Cuire asperges et pommes de terre.\n2. Émulsionner la Hollandaise au bain-marie.",
        "dressage": "Assiette allongée, asperges nappées de Hollandaise, pommes de terre à côté."
    },
    {
        "nom": "7. Hackbraten", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 20 min | Cuisson : 35 min",
        "ingredients": "• 200g pain de viande hachée\n• 100g champignons sautés\n• 12cl sauce crème (Rahmsoße)\n• 150g spätzle au pesto d'ail des ours",
        "etapes": "1. Rôtir le pain de viande au four à 180°C (30 min).\n2. Sauter les champignons et lier la sauce.",
        "dressage": "Trancher le hackbraten, napper de sauce, accompagner des spätzle."
    },
    {
        "nom": "8. Gegrilltes Lachsfilet", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 10 min | Cuisson : 8 min",
        "ingredients": "• 200g pavé de saumon\n• 120g asperges vertes et blanches\n• 80g sauce Hollandaise | 150g pommes de terre",
        "etapes": "1. Cuire le saumon côté peau (à cœur ~52°C).\n2. Napper de sauce Hollandaise.",
        "dressage": "Lit d'asperges, pavé de saumon grillé par-dessus, napper de Hollandaise."
    },
    {
        "nom": "9. Cordon Bleu vom Kalb", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 15 min | Cuisson : 8 min",
        "ingredients": "• 200g escalope de veau | 40g jambon\n• 40g gruyère | Panure anglaise\n• 30g beurre clarifié",
        "etapes": "1. Garnir l'escalope, paner.\n2. Cuire au beurre clarifié à la poêle (4 min par face).",
        "dressage": "Cordon bleu entier, quartier de citron, frites et légumes."
    },
    {
        "nom": "10. Paniertes Schweineschnitzel", "resto": "Landgasthof Kreuz", "poste": "Saucier / Friture",
        "temps": "Préparation : 10 min | Cuisson : 6 min",
        "ingredients": "• 180g escalope de porc panée\n• 12cl sauce rôtie (Bratensoße)\n• 150g frites",
        "etapes": "1. Frire l'escalope panée jusqu'à dorure.\n2. Réchauffer la sauce rôtie.",
        "dressage": "Schnitzel croustillant, frites, sauce rôtie en saucière."
    },
    {
        "nom": "11. Zwiebelrostbraten vom Rinderrücken", "resto": "Landgasthof Kreuz", "poste": "Saucier / Viandes",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 220g pavé de bœuf | 150g oignons\n• 15cl fond de veau brun lié\n• 30g beurre clarifié",
        "etapes": "1. Saisir le bœuf à la poêle.\n2. Confire ou frire les oignons.",
        "dressage": "Pavé nappé de sauce, dôme d'oignons confits, frites."
    },
    {
        "nom": "12. Zanderfilets auf der Haut", "resto": "Landgasthof Kreuz", "poste": "Poisson",
        "temps": "Préparation : 15 min | Cuisson : 6 min",
        "ingredients": "• 180g filet de sandre | 100g champignons\n• 180g risotto à l'ail des ours\n• 20g beurre",
        "etapes": "1. Cuire le risotto.\n2. Cuire le sandre unilatéralement sur peau.",
        "dressage": "Risotto au centre, filet de sandre posé sur la peau."
    },
    {
        "nom": "13. Saure Leberle", "resto": "Landgasthof Kreuz", "poste": "Saucier",
        "temps": "Préparation : 10 min | Cuisson : 5 min",
        "ingredients": "• 180g foie émincé | 60g oignons\n• 40g cornichons | 3cl vinaigre de vin\n• 200g pommes de terre sautées",
        "etapes": "1. Sauter le foie et les oignons à feu vif.\n2. Déglacer au vinaigre, ajouter les cornichons.",
        "dressage": "Foie sauté nappé de sauce acidulée, pommes sautées."
    },
    {
        "nom": "14. Käsespätzle (hausgemachte)", "resto": "Landgasthof Kreuz", "poste": "Entremet / Pâtes",
        "temps": "Préparation : 25 min | Cuisson : 10 min",
        "ingredients": "• 200g spätzle frais | 90g fromage Fontanella\n• 50g oignons rissolés | Persil",
        "etapes": "1. Pocher les spätzle dans l'eau bouillante.\n2. Mélanger chaudement avec le fromage.",
        "dressage": "Spätzle fondants au fromage, parsemer d'oignons rissolés."
    },
    {
        "nom": "15. Veganes gelbes Kokos-Curry", "resto": "Landgasthof Kreuz", "poste": "Légumier",
        "temps": "Préparation : 20 min | Cuisson : 20 min",
        "ingredients": "• 15cl lait de coco | 20g curry jaune\n• 100g asperges | 120g légumes\n• 180g pommes de terre au four",
        "etapes": "1. Rissoler et mijoter dans le curry coco (15 min).\n2. Cuire les pommes de terre.",
        "dressage": "Curry de légumes onctueux, pommes de terre rôties à côté."
    },
    {
        "nom": "16. Cremiges Spargel-Risotto", "resto": "Landgasthof Kreuz", "poste": "Entremet",
        "temps": "Préparation : 10 min | Cuisson : 20 min",
        "ingredients": "• 100g riz Arborio | 40cl bouillon\n• 100g asperges | 30g fromage dur\n• 20g beurre",
        "etapes": "1. Nacrer le riz, mouiller au bouillon.\n2. Crémer au beurre et fromage.",
        "dressage": "Risotto étalé, pointes d'asperges en décor."
    },
    {
        "nom": "17. Wurstsalat (Klassisch)", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g saucisse de Lyon en lanières\n• 50g oignons | 40g cornichons\n• 4cl vinaigrette | Pain",
        "etapes": "1. Mélanger les ingrédients et mariner 10 min.",
        "dressage": "Salade de saucisses marinée, pain frais à part."
    },
    {
        "nom": "18. Schweizer Wurstsalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 120g saucisse | 80g Emmental\n• 50g oignons | Marinade | Pain",
        "etapes": "1. Mélanger saucisse, fromage et marinade.",
        "dressage": "Mélange lanières saucisse/fromage, oignons, pain."
    },
    {
        "nom": "19. Vegetarischer Käsesalat", "resto": "Landgasthof Kreuz", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g fromage en lamelles | Oignons\n• Cornichons | Vinaigrette | Pain",
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
        "ingredients": "• 100g petite escalope | 100g frites\n• 50g crudités",
        "etapes": "1. Cuire escalope et frites.",
        "dressage": "Schnitzel, frites et crudités."
    },
    {
        "nom": "23. Apfelstrudel", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie",
        "temps": "Cuisson : 12 min",
        "ingredients": "• 1 part de strudel | 1 boule vanille\n• 30g chantilly",
        "etapes": "1. Réchauffer le strudel au four à 180°C.",
        "dressage": "Strudel chaud, glace vanille, chantilly."
    },
    {
        "nom": "24. Nuss-Krokant-Becher", "resto": "Landgasthof Kreuz", "poste": "Pâtisserie / Glacier",
        "temps": "Préparation : 5 min",
        "ingredients": "• 2 boules glace noisette | 20g krocant\n• 20g noix caramélisées | Sirop | Chantilly",
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
        "ingredients": "• 100g compotée | 60g mascarpone\n• 30g crumble | 1 boule vanille",
        "etapes": "1. Superposer compotée, mascarpone et crumble.",
        "dressage": "Assiette creuse, textures harmonieuses."
    },

    # --- Hof Höfen ---
    {
        "nom": "27. Pommes terre & légumes truffe", "resto": "Hof Höfen", "poste": "Garde-manger / Friture",
        "temps": "Cuisson : 5 min",
        "ingredients": "• 180g pommes de terre | 30g roquette\n• 40g mayo végane à la truffe",
        "etapes": "1. Frire les pommes de terre.",
        "dressage": "Pommes de terre croustillantes, roquette dessus, mayo à part."
    },
    {
        "nom": "28. Légumes véganes au four", "resto": "Hof Höfen", "poste": "Légumier",
        "temps": "Cuisson : 25 min",
        "ingredients": "• 220g légumes racines | 50g houmous\n• 10g graines grillées",
        "etapes": "1. Rôtir au four à 180°C.",
        "dressage": "Légumes rôtis chauds, houmous, graines."
    },
    {
        "nom": "29. Spätzle au fromage Hof Höfen", "resto": "Hof Höfen", "poste": "Entremet",
        "temps": "Cuisson : 8 min",
        "ingredients": "• 220g spätzle maison | 80g fromage\n• 40g oignons rissolés",
        "etapes": "1. Mélanger les spätzle chauds avec le fromage.",
        "dressage": "Poêlon ou assiette creuse, oignons rissolés par-dessus."
    },
    {
        "nom": "30. Saucisses sauvages de Rommel", "resto": "Hof Höfen", "poste": "Grill / Saucier",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 1 paire de saucisses de gibier (180g)\n• 200g salade de pommes de terre",
        "etapes": "1. Cuire à la plancha ou poêle douce.",
        "dressage": "Assiette rectangulaire, saucisses en diagonale, salade tiède."
    },
    {
        "nom": "31. Escalope de porc panée", "resto": "Hof Höfen", "poste": "Friture / Saucier",
        "temps": "Cuisson : 6 min",
        "ingredients": "• 180g escalope panée | 150g frites\n• 10cl sauce",
        "etapes": "1. Cuire l'escalope et l'accompagnement.",
        "dressage": "Schnitzel croustillant, frites, sauce."
    },
    {
        "nom": "32. Poitrine de porc rôtie", "resto": "Hof Höfen", "poste": "Saucier / Rôti",
        "temps": "Cuisson : 45 min",
        "ingredients": "• 220g poitrine de porc | 12cl jus corsé\n• 200g salade de pommes de terre",
        "etapes": "1. Rôtir lentement, finir au grill pour la couenne.",
        "dressage": "Tranche de poitrine croustillante, jus, salade."
    },
    {
        "nom": "33. Ragoût de venaison braisée", "resto": "Hof Höfen", "poste": "Saucier / Mijotés",
        "temps": "Cuisson : 10 min",
        "ingredients": "• 200g ragoût de gibier | 180g spätzle\n• 30g canneberges",
        "etapes": "1. Réchauffer le ragoût, sauter les spätzle.",
        "dressage": "Spätzle au fond, ragoût nappé, cuillère de canneberges."
    },
    {
        "nom": "34. Salade de saucisses badoise", "resto": "Hof Höfen", "poste": "Garde-manger",
        "temps": "Préparation : 10 min",
        "ingredients": "• 180g saucisse, oignons, vinaigrette\n• 150g frites",
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
        "ingredients": "• 200g pâte à crêpe épaisse pochée\n• Sucre, compote de pommes",
        "etapes": "1. Caraméliser les morceaux au beurre et sucre.",
        "dressage": "Morceaux saupoudrés de sucre glace, compote à part."
    },
    {
        "nom": "37. Crème de la forêt de Baden", "resto": "Hof Höfen", "poste": "Pâtisserie",
        "temps": "Préparation : 5 min",
        "ingredients": "• 120g crème au miel (romarin/thym)\n• Sirop de miel, physalis",
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

def main(page: ft.Page):
    page.title = "Rommel Chef Mobile"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0e1117"
    page.padding = 20

    fiches_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def charger_fiches(filtre_resto="Tous"):
        fiches_column.controls.clear()
        for plat in menus_data:
            if filtre_resto != "Tous" and plat["resto"] != filtre_resto:
                continue
            
            card = ft.Container(
                content=ft.Column([
                    ft.Text(plat["nom"], size=16, weight=ft.FontWeight.BOLD, color="#58a6ff"),
                    ft.Text(f"📍 {plat['resto']} | ⚙️ {plat['poste']}", size=11, color="#8b949e"),
                    ft.Text(f"⏱️ {plat['temps']}", size=11, italic=True, color="#d29922"),
                    ft.Divider(color="#30363d"),
                    ft.Text(f"🧪 Ingrédients :\n{plat['ingredients']}", size=12, color="#c9d1d9"),
                    ft.Text(f"🔥 Préparation :\n{plat['etapes']}", size=12, color="#c9d1d9"),
                    ft.Text(f"🍽️ Dressage : {plat['dressage']}", size=12, weight=ft.FontWeight.W_500, color="#7ee787"),
                ]),
                bgcolor="#161b22",
                padding=12,
                border_radius=8,
                border=ft.border.all(1, "#30363d"),
                margin=ft.margin.only(bottom=8)
            )
            fiches_column.controls.append(card)
        page.update()

    charger_fiches()

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(
                text="Fiches Pro",
                icon=ft.icons.MENU_BOOK,
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.ElevatedButton("Tous (39)", on_click=lambda e: charger_fiches("Tous")),
                            ft.ElevatedButton("Kreuz", on_click=lambda e: charger_fiches("Landgasthof Kreuz")),
                            ft.ElevatedButton("Höfen", on_click=lambda e: charger_fiches("Hof Höfen")),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Divider(color="transparent"),
                        fiches_column
                    ]),
                    padding=5
                )
            ),
            ft.Tab(
                text="Quiz Flashcard",
                icon=ft.icons.PSYCHOLOGY,
                content=ft.Container(
                    content=ft.Text("Mode Quiz mobile actif", color="white"),
                    padding=20
                )
            )
        ],
        expand=1
    )

    page.add(
        ft.Text("🍳 Rommel Chef Academy (39 Menus)", size=18, weight=ft.FontWeight.BOLD, color="white"),
        tabs
    )

if __name__ == "__main__":
    ft.app(target=main)