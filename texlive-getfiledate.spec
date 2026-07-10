%global tl_name getfiledate
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Find the date of last modification of a file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/getfiledate
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/getfiledate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package fetches from the system the date of last modification or
opening of an existing file, using the function \pdffilemoddate (present
in recent versions of pdfTeX); the user may specify how the date is to
be presented.

