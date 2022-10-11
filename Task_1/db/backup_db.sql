PGDMP                     	    z            Task_1    14.5    14.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16441    Task_1    DATABASE     e   CREATE DATABASE "Task_1" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "Task_1";
                postgres    false            �            1259    16455 	   addresses    TABLE     `   CREATE TABLE public.addresses (
    id integer NOT NULL,
    address character(100) NOT NULL
);
    DROP TABLE public.addresses;
       public         heap    postgres    false            �            1259    16443    ads    TABLE     �   CREATE TABLE public.ads (
    id integer NOT NULL,
    name character(100) NOT NULL,
    author_id integer NOT NULL,
    price numeric NOT NULL,
    description character(500),
    address_id integer NOT NULL,
    is_published boolean NOT NULL
);
    DROP TABLE public.ads;
       public         heap    postgres    false            �            1259    16449    authors    TABLE     Z   CREATE TABLE public.authors (
    id integer NOT NULL,
    name character(30) NOT NULL
);
    DROP TABLE public.authors;
       public         heap    postgres    false            �          0    16455 	   addresses 
   TABLE DATA           0   COPY public.addresses (id, address) FROM stdin;
    public          postgres    false    211   9       �          0    16443    ads 
   TABLE DATA           `   COPY public.ads (id, name, author_id, price, description, address_id, is_published) FROM stdin;
    public          postgres    false    209          �          0    16449    authors 
   TABLE DATA           +   COPY public.authors (id, name) FROM stdin;
    public          postgres    false    210   +       h           2606    16459    addresses addresses_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.addresses DROP CONSTRAINT addresses_pkey;
       public            postgres    false    211            d           2606    16447    ads ads_pkey 
   CONSTRAINT     J   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT ads_pkey PRIMARY KEY (id);
 6   ALTER TABLE ONLY public.ads DROP CONSTRAINT ads_pkey;
       public            postgres    false    209            f           2606    16453    authors authors_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.authors DROP CONSTRAINT authors_pkey;
       public            postgres    false    210            j           2606    16475    ads fk_address    FK CONSTRAINT     ~   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT fk_address FOREIGN KEY (address_id) REFERENCES public.addresses(id) NOT VALID;
 8   ALTER TABLE ONLY public.ads DROP CONSTRAINT fk_address;
       public          postgres    false    3176    209    211            i           2606    16470    ads fk_author    FK CONSTRAINT     z   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES public.authors(id) NOT VALID;
 7   ALTER TABLE ONLY public.ads DROP CONSTRAINT fk_author;
       public          postgres    false    210    209    3174            �   �   x���M
�0���)r �ت��0�]((�[JWn�j����n䴂(t�HxɃ|3��\��2��F�j��#Eɵ��=���X��5.����Cy}	%£���9�}�}�D���4CrC%d���lS�V{�����s}�ӠS��h����|&��W�R�`�����($�2m�~/:N�
�?)Բg�v���UJ� �3�      �     x��[�n�]���jg��DY�]~ �d��$$�ao� ى�eѐlBi��3	�,��l�M��!_0��:����R���~��,���}��:u��ߧqz���n�I�i?�9�o��e�l/��ܦK�4�:��a�wK��͠�n4��U���ҁt���ʣ����hj.��a�7�2�����o�M_f�i�N�c|���(�\;iq_>��=�{�V��;it�H�x��9�IG�l_:��Y�?1������D��&h��t �#��Iz.m<�9��/3C�W����@n��������$;�n"�=�����������:H���8HY����a�N�GNF^��-$�O������
Z����� �廐#��v�cO�ZvG�5�%�uw�C���b&?Ȧ�A�`a�7��?�Wbb03�5�D�c5�9��Fʍ�I�9��>t�P�Bi<�]��q0³he�8�a.�}yLL�&"�߀���D�b��,���.gƏv��cٕ��w��v��h����X��w����wB6'0+0%���|M�+`�Oȡ<��_�ӥ�!o/�����Û�:?�+��n�k�;�cF�vtJX)nv�G�� 0�昧J`Z�q��'�����I^�p�e���=�뿿3��`n��R{oM��J�V)Φ��`5����a��<[�A�V.��}��������w����W���^����������;v_ݻ{{I�7h�_}F��{H'o'��L�"���ī������_x��7����#gy.��g��Jn�Pwi�HK��P,�r�i"�\� �KN_�m}���4ػ�M|�K�����f.rp?����.����K�{[�m�� �����<}�|�
�~!����DL�$>�f8/f\!d��?�Ŭ�z��O�)-|c-X���ft\��=0��J~�h�:��t�*W\_�ڮ�K��N���&��f�^$~N���Xw�ڞ�n`/�� &D2)�`�G"��ՙW�w���S�i*��ς[��OH ��
A�r��~��jN�I�A'�S��B]�Hl�4Ӕby����w.T��~pP���D|NB7�{sF�v= ����Ж�t\�
c�p�)��(�D�Ł>.k�3��z`?1�X(�ɐ)�D��>�Ab��&YU���������hn��^�I$SY�يJ׌���i�G.;� �n
I��gy��nBH� ����\�/�
�A���c�߱���-�H6��s-'U9�K˸�`}|�|�@�i��Tn�R82MI`j5c�%}��"!��k�+���b��e�܅��Q*BoEdf��9�ѡ�q}�|�H��+9������-�W�Tŏ������PNɔA1#����w�TDN�`ʓ�Ż+�*;oG��[�(t�b/H�0�Y��8�0�9����D��/L�}�Յ�8KT�d8�.�_О0��z|���]�6E?��1�4d��e/�b�oը�L��L���G�3ϳ'��1�Y^�b�V��D���oD�,
:A_a��\~�%AF�!I8J<��#��>B3�vI�;��,�����Q�36���2�������Ę�^k6Y�����K�z�c�g̊�����hI�hm5�b��uЄ{i}� ��"��)+Z����zfiZ��3E¸���r����s��  $v���Ƭ@�
�9�˜���Jp]�C1V^Z55\Z�I�]0Ñ0�[ϡVĥu-9�-E��9�R#}��1��#G�F�Y)�!��?��T�O�1+&P��Oa|�j�/{�?�K�e�aDA�㈙CF�����j;A+؂ͼ6'�G6�E!�-z��u/,mX�J�B+�6*�c�����x)W�@i�x)��x��!5�	�*Z}�-�/��`yO�%�7&�T�[��ր�{�q�@<�Z.ݘ��V��+�y��C�H�t�S�/��	��[�j|�Ԩ�sI2횮iW�����ҷ�XfفFǹ�2ޘ;��@1`���\A��V�TK[ޕ&��a�3zС���K���5l#C8�O�
6a�[��b��N���I
��5g�:�aq(41)�R�G̔~�`ZA��ȏ
X*G�+E	�HyP��j���+�$�Lk9a��_9�N�O��e���\oݽ�t&�͆���:��8V[^�U��	]
�v�~Ð�s�~Kڝa3���Ł����������¾�|&���(�_�)yA@�'9Mb|�]��C�=Fz����!�go�B�')~��nnމ1xLo6���+������P���.k$�7����;����,��E���-Q�ʡ2�T��;�E�~y�;��z����6-0a�u�i";f�+�v�4������;7%ĭ��c]��7oB�
y����k1{�h�*�.qmU�Τ�r�M�:�ЙǎY zdK��=�M��	�y=��E��TJk�q4��T7_H0 W��q����N#-�x�_hL>�բhd�yV%��ꪴ�4�MqlwȢ��6Î�X����aYv7WSԙ"�����T�ꮴ�U����z2(�+���H ��/��*0��5�]��J�×�R�icRɉ�Z�}�j26,UCL&�ʹV�q�?͝|A���&gB�bz	�"{�2�l���Q���w�yle0�.p1����R�B�|���`� Q�����K^���2��������k͝�Ƈ��z"�f�_f�̣�yߛAss�@޹�n�k�s�8���*o�1g`R�x�w��>�ϥV͖(�U��,��E��$#��L7�T���O!�P�z�͇y��H�X�[;�X�ƍ�I�|��Idu�n���P��3�=U5��OV?�X���͛%�ͩ�$������g&֋�`�s��Q:-�����,Xp��������:�yZJ��<�F3�C��
·s�,Ź��q��l��Pn'2�/]s��ōF�~U�fnkcۉ�����)��
p������{M8�5��D��4�:}&ϤC��{-��!w��8K_�,�]/Ҿ�?�ƭ��� e�MƘ�@�+Í�(��2�_��WOro��h>!�K����R��͜�x¸1����h�#`E ��U����̇��+����L2�3���.�$Z��"k�UV��1�Q~ÞX�+ g���S�-2�V�G��I��|����t2�Tyz���KzWT6+�2qFE)���Z2O<�
N������]F���B2��oǟ<�5dO�x
���L0%��)i��Jj��0�Cv̳g8��2wQ�Nx���Еb/<۩J_A/�Ղx��E��V}mm��V4sP      �   f   x�}��	�0���n�@�Y���t����Sä#7w�9�OK����+�|�;�!�Fԑ��p��B@Ґᡪڳ�1<V�b���j"�L����57���FN     