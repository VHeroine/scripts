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
    c_ZERO     constant varchar2(8) := '����';
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
           when 1 then ' ���'
           when 2 then ' ������'
           when 3 then ' ������'
           when 4 then ' ���������'
           when 5 then ' �������'
           when 6 then ' ��������'
           when 7 then ' �������'
           when 8 then ' ���������'
           when 9 then ' ���������'
           else ''
         end ||
         case l_d_2
           when 2 then ' ��������'
           when 3 then ' ��������'
           when 4 then ' �����'
           when 5 then ' ���������'
           when 6 then ' ����������'
           when 7 then ' ���������'
           when 8 then ' �����������'
           when 9 then ' ���������'
           else ''
         end ||
         case l_d_1
           when 1 then
             case when l_thousand = 1 or 1=0
               then ' ����'
               else ' ����'
             end
           when 2 then
             case when l_thousand = 1 or 1=0
               then ' ���'
               else ' ���'
             end
           when 3 then ' ���'
           when 4 then ' ������'
           when 5 then ' ����'
           when 6 then ' �����'
           when 7 then ' ����'
           when 8 then ' ������'
           when 9 then ' ������'
           when 10 then ' ������'
           when 11 then ' �����������'
           when 12 then ' ����������'
           when 13 then ' ����������'
           when 14 then ' ������������'
           when 15 then ' ����������'
           when 16 then ' �����������'
           when 17 then ' ����������'
           when 18 then ' ������������'
           when 19 then ' ������������'
           else ''
         end ||
         case l_thousand
           when 2 then ' �����' ||
             case
               when l_d_1 = 1
                 then '�'
               when l_d_1 in (2, 3, 4)
                 then '�'
               else ''
             end
           when 3 then ' �������'
           when 4 then ' ��������'
           when 5 then ' ��������'
           when 6 then ' ����������'
           when 7 then ' ����������'
           else ''
         end ||
         case
           when l_thousand in (3, 4, 5, 6, 7) then
             case
               when l_d_1 = 1 then ''
               when l_d_1 in (2, 3, 4) then '�'
               else '��'
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
