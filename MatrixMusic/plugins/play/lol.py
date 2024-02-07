import random
import re
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import BOT_TOKEN
from database import set_db_waitg, get_db_waitg, del_db_waitg, set_db_mypointgame
from MatrixMusic.plugins.play.locks import lock_games_test, set_db_wait, lock_myphoto_test


if m.text == "عقاب" or m.text == "لعبه عقاب" or m.text == "لعبة عقاب" or m.text == "العاب عقاب":
        if not lock_games_test(m):
            eqab = [
                    
                "↯︙صورة وجهك او رجلك او خشمك او يدك\n↯",
                "↯︙اصدر اي صوت يطلبه منك الاعبين\n↯",
                "↯︙سكر خشمك و قول كلمة من اختيار الاعبين الي معك\n↯",
                "↯︙روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبين  الحد الاقصى 3 رسائل\n↯",
                "↯︙قول نكتة اذا و ??ازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية\n↯",
                "↯︙سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك\n↯",
                "↯︙ذي المرة لك لا تعيدها\n↯",
                "↯︙ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام\n↯",
                "↯︙صور اي شيء يطلبه منك الاعبين\n↯",
                "↯︙اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل....\n↯",
                "↯︙سكر خشمك و قول كلمة من اختيار الاعبين الي معك\n↯",
                "↯︙سو مشهد تمثيلي عن مصرية بتولد\n↯",
                "↯︙اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف\n↯",
                "↯︙ذي المرة لك لا تعيدها\n↯",
                "↯︙ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام\n↯",
                "↯︙روح عند اي احد بالخاص و قول له انك تحبه و الخ\n↯",
                "↯︙اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص\n↯",
                "↯︙قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية\n↯",
                "↯︙سامحتك خلاص مافيه عقاب لك :slight_smile:\n↯",
                "↯︙اتصل على احد من اخوياك  خوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك\n↯",
                "↯︙غير اسمك الى اسم من اختيار الاعبين الي معك\n↯",
                "↯︙اتصل على امك و قول لها انك تحبها :heart:\n↯",
                "↯︙لا يوجد سؤال لك سامحتك :slight_smile:\n↯",
                "↯︙قل لواحد ماتعرفه عطني كف\n↯",
                "↯︙منشن الجميع وقل انا اكرهكم\n↯",
                "↯︙اتصل لاخوك و قول له انك سويت حادث و الخ....\n↯",
                "↯︙روح المطبخ و اكسر صحن او كوب\n↯",
                "↯︙اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت ا??كف\n↯",
                "↯︙قول لاي بنت موجود في الروم كلمة حلوه\n↯",
                "↯︙تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني\n↯",
                "↯︙لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر\n↯",
                "↯︙قول قصيدة \n↯",
                "↯︙تكلم باللهجة السودانية الين يجي دورك مرة ثانية\n↯",
                "↯︙اتصل على احد من اخوياك  خوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك\n↯",
                "↯︙اول واحد تشوفه عطه كف\n↯",
                "↯︙سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين\n↯",
                "↯︙سامحتك خلاص مافيه عقاب لك :slight_smile:\n↯",
                "↯︙اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل....\n↯",
                "↯︙روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك\n↯",
                "↯︙تاخذ عقابين\n↯",
                "↯︙قول اسم امك افتخر بأسم امك\n↯",
                "↯︙ار??ي اي شيء قدامك على اي احد موجود او على نفسك\n↯",
                "↯︙اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك\n↯",
                "↯︙اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه\n↯",
                "↯︙تتصل على الوالده  و تقول لها خطفت شخص\n↯",
                "↯︙ تتصل على الوالده  و تقول لها تزوجت با سر\n↯",
                "↯︙????تصل على الوالده  و تقول لها  احب وحده\n↯",
                "↯︙تتصل على شرطي تقول له عندكم مطافي\n↯",
                "↯︙خلاص سامحتك\n↯",
                "↯︙ تصيح في الشارع انا  مجنوون\n↯",
                "↯︙ تروح عند شخص تقول له احبك\n↯"

            ]
            await m.reply_text(random.choice(eqab), reply_to_message_id=m.message_id)
            set_db_wait("eqab", m.from_user.id, m.chat.id)
      
