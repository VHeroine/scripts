create or replace package hr.convert_num_to_str is

  -- Author  : CHEZA
  -- Created : 26.05.2020 14:00:00
  -- Purpose : Convert numbers to text in the Russian language
  
  -- Public function and procedure declarations
  function convert_num_to_str(pr_num number   default null,
                              pr_str varchar2 default null)
    return varchar2 deterministic;

end convert_num_to_str;
/
create or replace package body hr.convert_num_to_str is

  -- Function and procedure implementations
  function convert_num_to_str(pr_num number   default null, /* as number: 1199.00 */
                              pr_str varchar2 default null) /* as string: '1199,00' or '1199.00' */
    return varchar2 deterministic is

    l_num      number;
    l_res      varchar2(32767) := cast(null as char);
    c_ZERO     constant varchar2(8) := 'Ноль';
    l_thousand number;
    l_ground   number;
    l_d_1      number;
    l_d_2      number;
    l_d_3      number;

  begin

    l_num := coalesce(pr_num, to_number(pr_str, regexp_replace(regexp_replace(pr_str, '\d', 9), '\,', 'D'), 'NLS_NUMERIC_CHARACTERS = '',.'''));

    if l_num = 0 then
      return c_ZERO;
    end if;

    while l_num > 0
      loop

        l_thousand := coalesce(l_thousand, 0) + 1;
        l_ground   := mod(l_thousand, 1000);
        l_num      := (l_num - l_ground) / 1000;

      if l_ground > 0 then
        l_d_3 := (l_ground- mod(l_ground, 100)) / 100;
        l_d_1 := mod(l_ground, 10);
        l_d_2 := (l_ground - l_d_3 * 100 - l_d_1) / 10;
        if l_d_2 = 1 then
          l_d_1 := 10 + l_d_1;
        end if;

       l_res :=
         case l_d_3
           when 1 then ' сто'
           when 2 then ' двести'
           when 3 then ' триста'
           when 4 then ' четыреста'
           when 5 then ' пятьсот'
           when 6 then ' шестьсот'
           when 7 then ' семьсот'
           when 8 then ' восемьсот'
           when 9 then ' девятьсот'
           else ''
         end ||
         case l_d_2
           when 2 then ' двадцать'
           when 3 then ' тридцать'
           when 4 then ' сорок'
           when 5 then ' пятьдесят'
           when 6 then ' шестьдесят'
           when 7 then ' семьдесят'
           when 8 then ' восемьдесят'
           when 9 then ' девяносто'
           else ''
         end ||
         case l_d_1
           when 1 then
             case when l_thousand = 1 or 1=0
               then ' одна'
               else ' один'
             end
           when 2 then
             case when l_thousand = 1 or 1=0
               then ' две'
               else ' два'
             end
           when 3 then ' три'
           when 4 then ' четыре'
           when 5 then ' пять'
           when 6 then ' шесть'
           when 7 then ' семь'
           when 8 then ' восемь'
           when 9 then ' девять'
           when 10 then ' десять'
           when 11 then ' одиннадцать'
           when 12 then ' двенадцать'
           when 13 then ' тринадцать'
           when 14 then ' четырнадцать'
           when 15 then ' пятнадцать'
           when 16 then ' шестнадцать'
           when 17 then ' семнадцать'
           when 18 then ' восемнадцать'
           when 19 then ' девятнадцать'
           else ''
         end ||
         case l_thousand
           when 2 then ' тысяч' ||
             case
               when l_d_1 = 1
                 then 'а'
               when l_d_1 in (2, 3, 4)
                 then 'и'
               else ''
             end
           when 3 then ' миллион'
           when 4 then ' миллиард'
           when 5 then ' триллион'
           when 6 then ' квадрилион'
           when 7 then ' квинтилион'
           else ''
         end ||
         case
           when l_thousand in (3, 4, 5, 6, 7) then
             case
               when l_d_1 = 1 then ''
               when l_d_1 in (2, 3, 4) then 'а'
               else 'ов'
             end
           else ''
         end ||
         coalesce(l_res, '');

      end if;

      end loop;

    return l_res;
  end;

end convert_num_to_str;
/
