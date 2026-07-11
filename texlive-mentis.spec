%global tl_name mentis
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	A basis for books to be published by Mentis publishers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mentis
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mentis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX class loads scrbook and provides changes necessary for
publishing at Mentis publishers in Paderborn, Germany. It is not an
official Mentis class, merely one developed by an author in close co-
operation with Mentis.

