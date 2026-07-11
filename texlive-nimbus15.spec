%global tl_name nimbus15
%global tl_revision 72894

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.015
Release:	%{tl_revision}.1
Summary:	Support files for Nimbus 2015 Core fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/nimbus15
License:	other-free lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nimbus15.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nimbus15.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(fontools)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Nimbus 2015 Core fonts added Greek and Cyrillic glyphs. This package
may be best suited as an add-on to the comprehensive Times package,
providing support for Greek and Cyrillic. A new intermediate weight of
NimbusMono (AKA Courier) is provided, along with a narrower version
which may be useful for rendering code.

